"""Aggregates all 7 days of JavaScript solutions, Junior explanations, helpers, and checkpoints,
and syncs them to the SQLite database.
"""

import os
import sys
import json
import sqlite3

backend_dir = os.path.dirname(os.path.abspath(__file__))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from database import get_db, recalculate_problem_mastery
from seed_data.day1_js import DAY_1_JS_DATA
from seed_data.day2_js import DAY_2_JS_DATA
from seed_data.day3_js import DAY_3_JS_DATA
from seed_data.day4_js import DAY_4_JS_DATA
from seed_data.day5_js import DAY_5_JS_DATA
from seed_data.day6_js import DAY_6_JS_DATA
from seed_data.day7_js import DAY_7_JS_DATA

def update_database_with_js():
    all_data = {}
    all_data.update(DAY_1_JS_DATA)
    all_data.update(DAY_2_JS_DATA)
    all_data.update(DAY_3_JS_DATA)
    all_data.update(DAY_4_JS_DATA)
    all_data.update(DAY_5_JS_DATA)
    all_data.update(DAY_6_JS_DATA)
    all_data.update(DAY_7_JS_DATA)

    print(f"[TOTAL CHECK] Loaded {len(all_data)} JavaScript problem solutions across all 7 days.")
    assert len(all_data) == 100, f"Expected 100 problems, got {len(all_data)}"

    conn = get_db()
    cursor = conn.cursor()

    updated_solutions = 0
    updated_checkpoints = 0

    for fid, item in all_data.items():
        cursor.execute("SELECT id FROM problems WHERE frontend_id = ?", (fid,))
        prob_row = cursor.fetchone()
        if not prob_row:
            print(f"[WARNING] Problem frontend_id {fid} not found in database!")
            continue

        p_id = prob_row['id']
        code_js = item.get('code_js', '')
        plain_exp = item.get('plain_explanation', '')
        helpers_json = json.dumps(item.get('js_helpers', []), ensure_ascii=False)

        # 1. Update problems description if present
        desc = item.get('description', '')
        if desc:
            cursor.execute("UPDATE problems SET description = ? WHERE id = ?", (desc, p_id))

        # 2. Update solutions table
        cursor.execute("""
            UPDATE solutions
            SET code_js = ?,
                plain_explanation = ?,
                js_helpers = ?
            WHERE problem_id = ?
        """, (code_js, plain_exp, helpers_json, p_id))
        updated_solutions += 1

        # 3. Update checkpoints (dynamic count & custom weights)
        checkpoints = item.get('checkpoints', [])
        if checkpoints:
            cursor.execute("SELECT dimension, completed FROM checkpoints WHERE problem_id = ?", (p_id,))
            existing_cps = {row['dimension']: row['completed'] for row in cursor.fetchall()}

            cursor.execute("DELETE FROM checkpoints WHERE problem_id = ?", (p_id,))

            for cp in checkpoints:
                dim = cp.get('dimension', 'point')
                is_comp = existing_cps.get(dim, 0)
                cursor.execute("""
                    INSERT INTO checkpoints (problem_id, dimension, title, detail, weight, completed)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (p_id, dim, cp['title'], cp['detail'], cp.get('weight', 20), is_comp))
                updated_checkpoints += 1

    conn.commit()
    conn.close()

    # Recalculate mastery
    for fid in all_data.keys():
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM problems WHERE frontend_id = ?", (fid,))
        p_row = cursor.fetchone()
        conn.close()
        if p_row:
            recalculate_problem_mastery(p_row['id'])

    print(f"[SUCCESS] Database update completed!")
    print(f"  - Total solutions updated: {updated_solutions} / 100")
    print(f"  - Total checkpoints registered: {updated_checkpoints} (4 per problem)")

if __name__ == "__main__":
    update_database_with_js()
