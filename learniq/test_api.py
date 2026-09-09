import requests
import json

SAMPLE_CONTENT = (
    "Photosynthesis is the process by which green plants, algae, and some bacteria "
    "convert light energy, usually from the sun, into chemical energy stored as glucose. "
    "This process occurs mainly in the chloroplasts using chlorophyll pigments. "
    "The overall equation is: 6CO2 + 6H2O + light energy -> C6H12O6 + 6O2."
)

def run_tests():
    base = "http://localhost:5000"

    # ── Test 1: Health ──────────────────────────────────────
    r = requests.get(base + "/api/health", timeout=10)
    assert r.status_code == 200
    assert r.json()["status"] == "ok"
    print("[PASS] GET /api/health ->", r.json())

    # ── Test 2: Missing content ─────────────────────────────
    r = requests.post(base + "/api/simplify", json={"content": "", "level": "Beginner"}, timeout=10)
    assert r.status_code == 400
    print("[PASS] Empty content returns 400 ->", r.json()["error"])

    # ── Test 3: Invalid level ───────────────────────────────
    r = requests.post(base + "/api/simplify", json={"content": "hello", "level": "Master"}, timeout=10)
    assert r.status_code == 400
    print("[PASS] Invalid level returns 400 ->", r.json()["error"])

    # ── Test 4: Full Beginner simplification ────────────────
    print("\n[RUNNING] POST /api/simplify  (Beginner)  — calling IBM Granite...")
    r = requests.post(base + "/api/simplify",
                      json={"content": SAMPLE_CONTENT, "level": "Beginner"},
                      timeout=90)
    assert r.status_code == 200, f"Expected 200, got {r.status_code}: {r.text[:200]}"
    data = r.json()
    assert data["success"] is True
    d = data["data"]

    # Validate all 7 required fields
    required = ["adapted_explanation", "key_concepts", "important_terms",
                "real_world_analogy", "example", "common_misconception", "quiz"]
    for field in required:
        assert field in d, f"Missing field: {field}"

    assert isinstance(d["key_concepts"], list) and len(d["key_concepts"]) > 0
    assert isinstance(d["important_terms"], list) and len(d["important_terms"]) > 0
    assert isinstance(d["quiz"], list) and len(d["quiz"]) == 3
    for q in d["quiz"]:
        assert "question" in q and "options" in q and "answer" in q and "explanation" in q

    print("[PASS] /api/simplify (Beginner) — all 7 fields present, quiz has 3 questions")
    print()
    print("  adapted_explanation :", d["adapted_explanation"][:90], "...")
    print("  key_concepts        :", d["key_concepts"])
    print("  important_terms     :", [(t["term"]) for t in d["important_terms"]])
    print("  real_world_analogy  :", d["real_world_analogy"][:70], "...")
    print("  example             :", d["example"][:70], "...")
    print("  common_misconception:", d["common_misconception"][:70], "...")
    print()
    for i, q in enumerate(d["quiz"]):
        print(f"  Q{i+1}: {q['question']}")
        for opt in q["options"]:
            marker = " [*]" if opt.strip().lower().startswith(q["answer"].strip()[:2].lower()) else "    "
            print(f"    {marker} {opt}")
        print(f"       Answer: {q['answer']}")
        print(f"       Explanation: {q['explanation'][:70]}")
        print()

    # ── Test 5: Expert level ────────────────────────────────
    print("[RUNNING] POST /api/simplify  (Expert)  — calling IBM Granite...")
    r2 = requests.post(base + "/api/simplify",
                       json={"content": SAMPLE_CONTENT, "level": "Expert"},
                       timeout=90)
    assert r2.status_code == 200
    d2 = r2.json()["data"]
    assert "adapted_explanation" in d2
    print("[PASS] /api/simplify (Expert) — response received")
    print("  Expert explanation  :", d2["adapted_explanation"][:90], "...")

    print()
    print("=" * 60)
    print("  ALL 5 TESTS PASSED — LEARNIQ is fully operational")
    print("  Open http://localhost:5000 in your browser")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
