import os
import sys

# Ensure backend folder is in sys.path
backend_dir = os.path.dirname(os.path.abspath(__file__))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from database import init_db, get_db
from seed_data.day1 import DAY_1_PROBLEMS
from seed_data.day2 import DAY_2_PROBLEMS
from seed_data.day3 import DAY_3_PROBLEMS
from seed_data.day4 import DAY_4_PROBLEMS
from seed_data.day5 import DAY_5_PROBLEMS
from seed_data.day6 import DAY_6_PROBLEMS
from seed_data.day7 import DAY_7_PROBLEMS

ALL_DAYS = [
    DAY_1_PROBLEMS,
    DAY_2_PROBLEMS,
    DAY_3_PROBLEMS,
    DAY_4_PROBLEMS,
    DAY_5_PROBLEMS,
    DAY_6_PROBLEMS,
    DAY_7_PROBLEMS
]

def run_seed():
    print(">>> 正在初始化 SQLite 数据库与数据表...")
    init_db()
    conn = get_db()
    cursor = conn.cursor()

    total_prob_count = 0
    total_cp_count = 0

    print(">>> 正在灌入 LeetCode Hot 100 全量数据与原子化微检查点...")
    for day_idx, day_problems in enumerate(ALL_DAYS, start=1):
        print(f"    - 正在灌入 Day {day_idx} (共 {len(day_problems)} 题)...")
        for item in day_problems:
            # 1. 插入或忽略题目
            cursor.execute("""
                INSERT INTO problems (frontend_id, title_cn, title_en, slug, difficulty, category, day)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(frontend_id) DO UPDATE SET
                    title_cn = excluded.title_cn,
                    title_en = excluded.title_en,
                    slug = excluded.slug,
                    difficulty = excluded.difficulty,
                    category = excluded.category,
                    day = excluded.day
            """, (
                item["frontend_id"],
                item["title_cn"],
                item["title_en"],
                item["slug"],
                item["difficulty"],
                item["category"],
                item["day"]
            ))
            
            # 获取对应的 problem_id
            cursor.execute("SELECT id FROM problems WHERE frontend_id = ?", (item["frontend_id"],))
            problem_id = cursor.fetchone()["id"]
            total_prob_count += 1

            # 2. 插入或更新最优解
            sol = item["solution"]
            cursor.execute("""
                INSERT INTO solutions (problem_id, core_insight, traps, time_complexity, space_complexity, code_python)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(problem_id) DO UPDATE SET
                    core_insight = excluded.core_insight,
                    traps = excluded.traps,
                    time_complexity = excluded.time_complexity,
                    space_complexity = excluded.space_complexity,
                    code_python = excluded.code_python
            """, (
                problem_id,
                sol["core_insight"],
                sol["traps"],
                sol["time_complexity"],
                sol["space_complexity"],
                sol["code_python"]
            ))

            # 3. 检查点（如果已经存在就不重复覆盖完成状态，否则插入）
            for cp in item["checkpoints"]:
                cursor.execute("""
                    SELECT id FROM checkpoints 
                    WHERE problem_id = ? AND dimension = ?
                """, (problem_id, cp["dimension"]))
                existing = cursor.fetchone()
                if not existing:
                    cursor.execute("""
                        INSERT INTO checkpoints (problem_id, dimension, title, detail, weight, completed)
                        VALUES (?, ?, ?, ?, ?, 0)
                    """, (
                        problem_id,
                        cp["dimension"],
                        cp["title"],
                        cp["detail"],
                        cp.get("weight", 25)
                    ))
                else:
                    # 更新描述文字与标题，保留已完成状态
                    cursor.execute("""
                        UPDATE checkpoints 
                        SET title = ?, detail = ?, weight = ?
                        WHERE id = ?
                    """, (cp["title"], cp["detail"], cp.get("weight", 25), existing["id"]))
                total_cp_count += 1

    conn.commit()
    conn.close()

    print("==================================================")
    print(f"[SUCCESS] Seeding complete! Populated {total_prob_count} problems and {total_cp_count} checkpoints.")
    print("==================================================")

if __name__ == "__main__":
    run_seed()
