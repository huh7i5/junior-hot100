import os
import sys
import json
from typing import Optional, List, Dict, Any
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

backend_dir = os.path.dirname(os.path.abspath(__file__))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from database import get_db, init_db, recalculate_problem_mastery, get_overview_stats

app = FastAPI(title="LeetCode Hot 100 Mastery API", version="1.0.0")

# 启用 CORS 允许前端跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class NoteUpdate(BaseModel):
    notes: str

class BatchToggleRequest(BaseModel):
    completed: bool

@app.on_event("startup")
def startup_event():
    init_db()

@app.get("/api/health")
def health_check():
    return {"status": "ok", "app": "Hot 100 Mastery API", "version": "1.0.0"}

@app.get("/api/overview")
def get_overview():
    return get_overview_stats()

@app.get("/api/problems")
def list_problems(
    day: Optional[int] = Query(None, description="Sprint Day (1-7)"),
    category: Optional[str] = Query(None, description="Category filter"),
    difficulty: Optional[str] = Query(None, description="Easy/Medium/Hard"),
    status: Optional[str] = Query(None, description="todo/in_progress/mastered"),
    search: Optional[str] = Query(None, description="Keyword search")
):
    conn = get_db()
    cursor = conn.cursor()

    query = """
        SELECT 
            p.id, p.frontend_id, p.title_cn, p.title_en, p.slug,
            p.difficulty, p.category, p.day, p.mastery_score, p.status,
            COUNT(c.id) as total_checkpoints,
            SUM(CASE WHEN c.completed = 1 THEN 1 ELSE 0 END) as completed_checkpoints
        FROM problems p
        LEFT JOIN checkpoints c ON p.id = c.problem_id
        WHERE 1=1
    """
    params = []

    if day is not None:
        query += " AND p.day = ?"
        params.append(day)
    if category:
        query += " AND p.category = ?"
        params.append(category)
    if difficulty:
        query += " AND p.difficulty = ?"
        params.append(difficulty)
    if status and status != "all":
        query += " AND p.status = ?"
        params.append(status)
    if search:
        search_pattern = f"%{search.strip()}%"
        query += " AND (p.title_cn LIKE ? OR p.title_en LIKE ? OR CAST(p.frontend_id AS TEXT) LIKE ?)"
        params.extend([search_pattern, search_pattern, search_pattern])

    query += " GROUP BY p.id ORDER BY p.day ASC, p.frontend_id ASC"
    cursor.execute(query, tuple(params))
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return rows

@app.get("/api/problems/{problem_id}")
def get_problem_detail(problem_id: int):
    conn = get_db()
    cursor = conn.cursor()

    # 查题目基本信息
    cursor.execute("SELECT * FROM problems WHERE id = ?", (problem_id,))
    prob_row = cursor.fetchone()
    if not prob_row:
        conn.close()
        raise HTTPException(status_code=404, detail="Problem not found")
    problem = dict(prob_row)

    # 查检查点列表
    cursor.execute("""
        SELECT id, dimension, title, detail, weight, completed, updated_at
        FROM checkpoints
        WHERE problem_id = ?
        ORDER BY id ASC
    """, (problem_id,))
    checkpoints = [dict(r) for r in cursor.fetchall()]

    # 查最优解题解
    cursor.execute("""
        SELECT core_insight, traps, time_complexity, space_complexity, code_python, code_js, plain_explanation, js_helpers
        FROM solutions
        WHERE problem_id = ?
    """, (problem_id,))
    sol_row = cursor.fetchone()
    solution = dict(sol_row) if sol_row else None
    if solution and solution.get('js_helpers') and isinstance(solution['js_helpers'], str):
        try:
            solution['js_helpers'] = json.loads(solution['js_helpers'])
        except Exception:
            pass

    conn.close()
    return {
        "problem": problem,
        "checkpoints": checkpoints,
        "solution": solution
    }

@app.post("/api/checkpoints/{checkpoint_id}/toggle")
def toggle_checkpoint(checkpoint_id: int):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id, problem_id, completed FROM checkpoints WHERE id = ?", (checkpoint_id,))
    cp = cursor.fetchone()
    if not cp:
        conn.close()
        raise HTTPException(status_code=404, detail="Checkpoint not found")

    new_state = 0 if cp["completed"] == 1 else 1
    cursor.execute("""
        UPDATE checkpoints 
        SET completed = ?, updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
    """, (new_state, checkpoint_id))
    conn.commit()
    conn.close()

    problem_id = cp["problem_id"]
    new_score, new_status = recalculate_problem_mastery(problem_id)
    overview = get_overview_stats()

    return {
        "success": True,
        "checkpoint_id": checkpoint_id,
        "completed": bool(new_state),
        "problem_id": problem_id,
        "mastery_score": new_score,
        "status": new_status,
        "overview": overview
    }

@app.post("/api/problems/{problem_id}/batch-toggle")
def batch_toggle_checkpoints(problem_id: int, req: BatchToggleRequest):
    conn = get_db()
    cursor = conn.cursor()

    val = 1 if req.completed else 0
    cursor.execute("""
        UPDATE checkpoints
        SET completed = ?, updated_at = CURRENT_TIMESTAMP
        WHERE problem_id = ?
    """, (val, problem_id))
    conn.commit()
    conn.close()

    new_score, new_status = recalculate_problem_mastery(problem_id)
    overview = get_overview_stats()

    return {
        "success": True,
        "problem_id": problem_id,
        "completed": req.completed,
        "mastery_score": new_score,
        "status": new_status,
        "overview": overview
    }

@app.put("/api/problems/{problem_id}/notes")
def update_problem_notes(problem_id: int, req: NoteUpdate):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE problems
        SET notes = ?, updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
    """, (req.notes, problem_id))
    conn.commit()
    conn.close()

    return {"success": True, "problem_id": problem_id}

@app.get("/api/export")
def export_progress():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id, frontend_id, mastery_score, status, notes, updated_at FROM problems")
    probs = [dict(r) for r in cursor.fetchall()]

    cursor.execute("SELECT id, problem_id, dimension, completed, updated_at FROM checkpoints")
    cps = [dict(r) for r in cursor.fetchall()]

    conn.close()
    return {
        "version": "1.0",
        "problems": probs,
        "checkpoints": cps
    }

# 静态资源挂载：如果前端已构建 dist，则挂载静态路由与 SPA 回退
frontend_dist = os.path.abspath(os.path.join(backend_dir, "..", "frontend", "dist"))
if os.path.exists(frontend_dist):
    app.mount("/assets", StaticFiles(directory=os.path.join(frontend_dist, "assets")), name="assets")

    @app.get("/{full_path:path}")
    async def serve_spa(full_path: str):
        # 排除以 api 开头的请求
        if full_path.startswith("api/"):
            raise HTTPException(status_code=404, detail="API route not found")
        file_path = os.path.join(frontend_dist, full_path)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            return FileResponse(file_path)
        return FileResponse(os.path.join(frontend_dist, "index.html"))

if __name__ == "__main__":
    import uvicorn
    print(">>> 启动 LeetCode Hot 100 Mastery 服务: http://127.0.0.1:8765")
    uvicorn.run("server:app", host="127.0.0.1", port=8765, reload=False)
