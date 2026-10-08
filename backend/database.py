import os
import sqlite3
from typing import Dict, Any, List, Optional

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "hot100.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    
    # 1. 题目表
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS problems (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        frontend_id INTEGER NOT NULL UNIQUE,
        title_cn TEXT NOT NULL,
        title_en TEXT NOT NULL,
        slug TEXT NOT NULL,
        difficulty TEXT NOT NULL,
        category TEXT NOT NULL,
        day INTEGER NOT NULL,
        mastery_score INTEGER DEFAULT 0,
        status TEXT DEFAULT 'todo',
        notes TEXT DEFAULT '',
        description TEXT DEFAULT '',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 2. 原子化检查点表 (每题4个标准维度: pattern, corner_case, solution, complexity)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS checkpoints (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        problem_id INTEGER NOT NULL,
        dimension TEXT NOT NULL,
        title TEXT NOT NULL,
        detail TEXT NOT NULL,
        weight INTEGER DEFAULT 25,
        completed INTEGER DEFAULT 0,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(problem_id) REFERENCES problems(id) ON DELETE CASCADE
    );
    """)

    # 3. 最优解与题解表
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS solutions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        problem_id INTEGER NOT NULL UNIQUE,
        core_insight TEXT NOT NULL,
        traps TEXT NOT NULL,
        time_complexity TEXT NOT NULL,
        space_complexity TEXT NOT NULL,
        code_python TEXT NOT NULL,
        code_java TEXT DEFAULT '',
        code_cpp TEXT DEFAULT '',
        code_js TEXT DEFAULT '',
        plain_explanation TEXT DEFAULT '',
        js_helpers TEXT DEFAULT '',
        FOREIGN KEY(problem_id) REFERENCES problems(id) ON DELETE CASCADE
    );
    """)

    # 动态检查并添加列 (兼容已有数据库迁移)
    cursor.execute("PRAGMA table_info(solutions)")
    existing_cols = [row["name"] for row in cursor.fetchall()]
    if "code_js" not in existing_cols:
        cursor.execute("ALTER TABLE solutions ADD COLUMN code_js TEXT DEFAULT ''")
    if "plain_explanation" not in existing_cols:
        cursor.execute("ALTER TABLE solutions ADD COLUMN plain_explanation TEXT DEFAULT ''")
    if "js_helpers" not in existing_cols:
        cursor.execute("ALTER TABLE solutions ADD COLUMN js_helpers TEXT DEFAULT ''")

    conn.commit()
    conn.close()

def recalculate_problem_mastery(problem_id: int):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(weight) as total_weight,
               SUM(CASE WHEN completed = 1 THEN weight ELSE 0 END) as done_weight
        FROM checkpoints
        WHERE problem_id = ?
    """, (problem_id,))
    row = cursor.fetchone()
    total_weight = row["total_weight"] or 100
    done_weight = row["done_weight"] or 0
    score = int(round((done_weight / total_weight) * 100))

    if score >= 100:
        status = "mastered"
    elif score > 0:
        status = "in_progress"
    else:
        status = "todo"

    cursor.execute("""
        UPDATE problems
        SET mastery_score = ?, status = ?, updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
    """, (score, status, problem_id))
    conn.commit()
    conn.close()
    return score, status

def get_overview_stats() -> Dict[str, Any]:
    conn = get_db()
    cursor = conn.cursor()

    # 题目总体统计
    cursor.execute("""
        SELECT 
            COUNT(*) as total_problems,
            SUM(CASE WHEN status = 'mastered' THEN 1 ELSE 0 END) as mastered_problems,
            SUM(CASE WHEN status = 'in_progress' THEN 1 ELSE 0 END) as in_progress_problems,
            SUM(CASE WHEN status = 'todo' THEN 1 ELSE 0 END) as todo_problems,
            AVG(mastery_score) as avg_mastery
        FROM problems
    """)
    prob_summary = dict(cursor.fetchone())

    # 检查点统计
    cursor.execute("""
        SELECT 
            COUNT(*) as total_checkpoints,
            SUM(CASE WHEN completed = 1 THEN 1 ELSE 0 END) as completed_checkpoints
        FROM checkpoints
    """)
    cp_summary = dict(cursor.fetchone())

    # 难度分布统计
    cursor.execute("""
        SELECT difficulty, COUNT(*) as total,
               SUM(CASE WHEN status = 'mastered' THEN 1 ELSE 0 END) as mastered,
               AVG(mastery_score) as avg_score
        FROM problems
        GROUP BY difficulty
    """)
    diff_stats = [dict(r) for r in cursor.fetchall()]

    # 7 天攻坚日历统计
    cursor.execute("""
        SELECT day, COUNT(*) as total,
               SUM(CASE WHEN status = 'mastered' THEN 1 ELSE 0 END) as mastered,
               SUM(CASE WHEN status = 'in_progress' THEN 1 ELSE 0 END) as in_progress,
               AVG(mastery_score) as avg_score
        FROM problems
        GROUP BY day
        ORDER BY day ASC
    """)
    day_stats = [dict(r) for r in cursor.fetchall()]

    # 知识专题统计
    cursor.execute("""
        SELECT category, COUNT(*) as total,
               SUM(CASE WHEN status = 'mastered' THEN 1 ELSE 0 END) as mastered,
               AVG(mastery_score) as avg_score
        FROM problems
        GROUP BY category
        ORDER BY total DESC
    """)
    category_stats = [dict(r) for r in cursor.fetchall()]

    conn.close()

    total_cp = cp_summary["total_checkpoints"] or 1
    done_cp = cp_summary["completed_checkpoints"] or 0
    overall_progress = round((done_cp / total_cp) * 100, 1)

    return {
        "summary": {
            "total_problems": prob_summary["total_problems"] or 0,
            "mastered_problems": prob_summary["mastered_problems"] or 0,
            "in_progress_problems": prob_summary["in_progress_problems"] or 0,
            "todo_problems": prob_summary["todo_problems"] or 0,
            "total_checkpoints": total_cp,
            "completed_checkpoints": done_cp,
            "overall_progress": overall_progress
        },
        "difficulty_stats": diff_stats,
        "day_stats": day_stats,
        "category_stats": category_stats
    }
