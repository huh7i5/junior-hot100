import os
import sys

backend_dir = os.path.dirname(os.path.abspath(__file__))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from starlette.testclient import TestClient
from server import app

client = TestClient(app)

def test_api():
    print("1. Testing /api/health ...")
    r = client.get("/api/health")
    assert r.status_code == 200, f"Health check failed: {r.text}"
    print("   -> OK:", r.json())

    print("2. Testing /api/overview ...")
    r = client.get("/api/overview")
    assert r.status_code == 200, f"Overview failed: {r.text}"
    overview = r.json()
    assert overview["summary"]["total_problems"] == 100
    assert overview["summary"]["total_checkpoints"] >= 400
    print(f"   -> OK: total 100 problems, {overview['summary']['total_checkpoints']} checkpoints verified!")

    print("3. Testing /api/problems (listing with day=1) ...")
    r = client.get("/api/problems?day=1")
    assert r.status_code == 200
    problems_day1 = r.json()
    assert len(problems_day1) == 17
    print(f"   -> OK: Day 1 has {len(problems_day1)} problems.")

    print("4. Testing /api/problems/{id} (problem 1 detail) ...")
    first_prob_id = problems_day1[0]["id"]
    r = client.get(f"/api/problems/{first_prob_id}")
    assert r.status_code == 200
    detail = r.json()
    assert len(detail["checkpoints"]) >= 4
    first_cp_weight = detail["checkpoints"][0]["weight"]
    assert "class Solution:" in detail["solution"]["code_python"]
    print(f"   -> OK: Problem '{detail['problem']['title_cn']}' has {len(detail['checkpoints'])} checkpoints and valid solution code.")

    print("5. Testing /api/checkpoints/{id}/toggle ...")
    cp_id = detail["checkpoints"][0]["id"]
    r = client.post(f"/api/checkpoints/{cp_id}/toggle")
    assert r.status_code == 200
    toggle_res = r.json()
    assert toggle_res["completed"] is True
    assert toggle_res["mastery_score"] == first_cp_weight
    assert toggle_res["status"] == "in_progress"
    print(f"   -> OK: Checkpoint toggled, problem score updated to {first_cp_weight}%, status 'in_progress'.")

    # Toggle it back to 0
    r = client.post(f"/api/checkpoints/{cp_id}/toggle")
    assert r.status_code == 200
    toggle_res = r.json()
    assert toggle_res["completed"] is False
    assert toggle_res["mastery_score"] == 0
    assert toggle_res["status"] == "todo"
    print("   -> OK: Checkpoint toggled back, score reset to 0%, status 'todo'.")

    print("6. Testing /api/problems/{id}/notes ...")
    r = client.put(f"/api/problems/{first_prob_id}/notes", json={"notes": "My test note for two sum"})
    assert r.status_code == 200
    r = client.get(f"/api/problems/{first_prob_id}")
    assert r.json()["problem"]["notes"] == "My test note for two sum"
    # Clean up test note
    client.put(f"/api/problems/{first_prob_id}/notes", json={"notes": ""})
    print("   -> OK: Notes update and retrieval verified.")

    print("\n==================================================")
    print(">>> ALL BACKEND API TESTS PASSED WITH 100% SUCCESS!")
    print("==================================================")

if __name__ == "__main__":
    test_api()
