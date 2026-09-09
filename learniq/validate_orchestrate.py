import json, sys, os

print("=== Validating orchestrate artefacts ===")
print()

# 1. tool_definition.json
with open("learniq/orchestrate/tool_definition.json") as f:
    td = json.load(f)
for k in ["name", "description", "input_schema", "output_schema", "endpoint"]:
    assert k in td, f"Missing key in tool_definition.json: {k}"
assert td["input_schema"]["required"] == ["content", "level"]
assert "adapted_explanation" in td["output_schema"]["properties"]
assert "quiz" in td["output_schema"]["properties"]
print("[PASS] tool_definition.json — all required keys and schemas present")

# 2. openapi_learniq.yaml
with open("learniq/orchestrate/openapi_learniq.yaml") as f:
    yaml_text = f.read()
for token in ["/api/simplify", "simplifyContent", "SimplifyRequest",
              "SimplifyData", "QuizQuestion", "Term",
              "Beginner", "Intermediate", "Advanced", "Expert"]:
    assert token in yaml_text, f"Missing in YAML: {token}"
print("[PASS] openapi_learniq.yaml — all paths, schemas, and level enums present")

# 3. deploy_agent.py
import ast
with open("learniq/orchestrate/deploy_agent.py") as f:
    code = f.read()
ast.parse(code)
for sym in ["learniq_ai_service", "get_or_create_space", "store_ai_service",
            "promote_to_space", "create_deployment", "main",
            "granite-4-h-small", "8e89e44d"]:
    assert sym in code, f"Missing in deploy_agent.py: {sym}"
print("[PASS] deploy_agent.py — syntax OK, all functions and config present")

# 4. README_DEPLOY.md
with open("learniq/orchestrate/README_DEPLOY.md") as f:
    md = f.read()
for section in ["Step 1", "Step 2", "Step 3", "Step 4", "Step 5",
                "openapi_learniq.yaml", "tool_definition.json",
                "deploy_agent.py", "Troubleshooting"]:
    assert section in md, f"Missing section in README: {section}"
print("[PASS] README_DEPLOY.md — all 5 steps and troubleshooting table present")

# 5. File structure
expected = [
    "learniq/orchestrate/openapi_learniq.yaml",
    "learniq/orchestrate/tool_definition.json",
    "learniq/orchestrate/deploy_agent.py",
    "learniq/orchestrate/README_DEPLOY.md",
    "learniq/app.py",
    "learniq/static/index.html",
    "learniq/requirements.txt",
]
for path in expected:
    assert os.path.exists(path), f"File missing: {path}"
print("[PASS] File structure — all 7 files present")

print()
print("ALL VALIDATIONS PASSED")
