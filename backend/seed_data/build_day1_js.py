# -*- coding: utf-8 -*-
"""Builder script to assemble and validate day1_js.py."""

import os
import sys
import pprint

backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from seed_data.day1_part1 import DAY_1_PART1
from seed_data.day1_part2 import DAY_1_PART2
from seed_data.day1_part3 import DAY_1_PART3
from seed_data.day1_part4 import DAY_1_PART4

ORDERED_PROBLEM_IDS = [
    1, 49, 128, 283, 11, 15, 42, 3, 438, 560, 239, 76, 53, 56, 189, 238, 41
]

combined = {}
combined.update(DAY_1_PART1)
combined.update(DAY_1_PART2)
combined.update(DAY_1_PART3)
combined.update(DAY_1_PART4)

print(f"Total problems collected: {len(combined)}")
assert len(combined) == 17, f"Expected 17 problems, got {len(combined)}"

# Validation
for pid in ORDERED_PROBLEM_IDS:
    assert pid in combined, f"Missing problem {pid}"
    p = combined[pid]
    
    # 1. Check metadata
    assert p.get("title_cn"), f"Problem {pid} missing title_cn"
    assert p.get("title_en"), f"Problem {pid} missing title_en"
    assert p.get("slug"), f"Problem {pid} missing slug"
    assert p.get("difficulty"), f"Problem {pid} missing difficulty"
    
    # 2. Check description
    desc = p.get("description", "")
    assert "### 题目描述" in desc, f"Problem {pid} description missing 题目描述"
    assert "### 示例" in desc, f"Problem {pid} description missing 示例"
    assert "### 提示与约束条件" in desc, f"Problem {pid} description missing 提示与约束条件"
    
    # 3. Check plain_explanation
    pe = p.get("plain_explanation", "")
    assert len(pe) >= 50, f"Problem {pid} plain_explanation too short ({len(pe)})"
    
    # 4. Check js_helpers
    helpers = p.get("js_helpers", [])
    assert len(helpers) >= 2, f"Problem {pid} js_helpers fewer than 2 ({len(helpers)})"
    for h in helpers:
        assert h.get("name"), f"Problem {pid} helper missing name"
        assert h.get("what_it_does"), f"Problem {pid} helper missing what_it_does"
        assert h.get("junior_tip"), f"Problem {pid} helper missing junior_tip"
        
    # 5. Check code_js
    code = p.get("code_js", "")
    assert "function" in code or "=>" in code, f"Problem {pid} code_js missing function declaration"
    assert "// TODO" not in code, f"Problem {pid} code_js contains TODO"
    assert "..." not in code, f"Problem {pid} code_js contains ..."
    
    # 6. Check checkpoints
    cps = p.get("checkpoints", [])
    assert 4 <= len(cps) <= 8, f"Problem {pid} checkpoints count {len(cps)} outside 4..8 range"
    weight_sum = 0
    for idx, cp in enumerate(cps, 1):
        assert cp.get("dimension") == f"point{idx}", f"Problem {pid} cp {idx} dimension is {cp.get('dimension')}, expected point{idx}"
        assert cp.get("title", "").startswith(f"知识点 {idx}："), f"Problem {pid} cp {idx} title format incorrect: {cp.get('title')}"
        assert len(cp.get("detail", "")) >= 20, f"Problem {pid} cp {idx} detail too short: {cp.get('detail')}"
        weight_sum += cp.get("weight", 0)
    assert weight_sum == 100, f"Problem {pid} checkpoint weights sum to {weight_sum}, expected 100!"

print("All 17 problems passed strict quality and specification checks!")

# Generate target file: day1_js.py
target_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "day1_js.py")

output_lines = []
output_lines.append('"""Day 1 JavaScript Solutions with Junior-level explanations, JS helpers, descriptions, and code-aligned checkpoints.')
output_lines.append('Auto-generated and strictly validated for LeetCode Hot 100 Mastery.')
output_lines.append('"""')
output_lines.append('')
output_lines.append('DAY_1_JS_DATA = {')

for pid in ORDERED_PROBLEM_IDS:
    p = combined[pid]
    output_lines.append(f'    {pid}: {{')
    output_lines.append(f'        "title_cn": {repr(p["title_cn"])},')
    output_lines.append(f'        "title_en": {repr(p["title_en"])},')
    output_lines.append(f'        "slug": {repr(p["slug"])},')
    output_lines.append(f'        "difficulty": {repr(p["difficulty"])},')
    
    # Description
    desc_escaped = p["description"].replace('"""', r'\"\"\"')
    output_lines.append(f'        "description": """{desc_escaped}""",')
    
    # Plain explanation
    pe_escaped = p["plain_explanation"].replace('"""', r'\"\"\"')
    output_lines.append(f'        "plain_explanation": """{pe_escaped}""",')
    
    # JS helpers
    output_lines.append('        "js_helpers": [')
    for h in p["js_helpers"]:
        output_lines.append('            {')
        output_lines.append(f'                "name": {repr(h["name"])},')
        output_lines.append(f'                "what_it_does": {repr(h["what_it_does"])},')
        output_lines.append(f'                "junior_tip": {repr(h["junior_tip"])},')
        output_lines.append('            },')
    output_lines.append('        ],')
    
    # Code JS
    code_escaped = p["code_js"].replace('"""', r'\"\"\"')
    output_lines.append(f'        "code_js": """{code_escaped}""",')
    
    # Checkpoints
    output_lines.append('        "checkpoints": [')
    for cp in p["checkpoints"]:
        output_lines.append('            {')
        output_lines.append(f'                "dimension": {repr(cp["dimension"])},')
        output_lines.append(f'                "title": {repr(cp["title"])},')
        output_lines.append(f'                "detail": {repr(cp["detail"])},')
        output_lines.append(f'                "weight": {cp["weight"]},')
        output_lines.append('            },')
    output_lines.append('        ],')
    output_lines.append('    },')

output_lines.append('}')
output_lines.append('')

with open(target_path, "w", encoding="utf-8") as f:
    f.write("\n".join(output_lines))

print(f"Successfully generated {target_path} (size: {os.path.getsize(target_path)} bytes)")
