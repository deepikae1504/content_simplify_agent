from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import json
import os

app = Flask(__name__, static_folder="static", template_folder="static")
CORS(app)

IBM_API_KEY = "X7aU8nnlcsoLboBZSNmOa0gni8DH68alaDwfeeqqL1k2"
IBM_URL = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"
PROJECT_ID = "8e89e44d-df10-4000-b8ef-9d5f2df5b19c"
MODEL_ID = "ibm/granite-4-h-small"

IAM_TOKEN_URL = "https://iam.cloud.ibm.com/identity/token"

_token_cache = {"token": None, "expires_at": 0}

def get_iam_token():
    import time
    if _token_cache["token"] and time.time() < _token_cache["expires_at"] - 60:
        return _token_cache["token"]

    resp = requests.post(
        IAM_TOKEN_URL,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={
            "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
            "apikey": IBM_API_KEY,
        },
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    _token_cache["token"] = data["access_token"]
    _token_cache["expires_at"] = time.time() + data.get("expires_in", 3600)
    return _token_cache["token"]


def build_prompt(content: str, level: str) -> str:
    level_descriptions = {
        "Beginner": "a complete newcomer with no prior knowledge, using very simple language, everyday analogies, and avoiding jargon entirely",
        "Intermediate": "someone who has basic familiarity with the subject and can handle some technical terms if explained",
        "Advanced": "someone with solid subject knowledge who appreciates technical depth and precise terminology",
        "Expert": "a domain specialist who values nuance, edge cases, and connections to cutting-edge research or practice",
    }
    audience = level_descriptions.get(level, level_descriptions["Intermediate"])

    return f"""You are LEARNIQ, an expert academic content simplification agent. Analyze the following course content and adapt it for {audience}.

Return your response as a valid JSON object with exactly these keys:
{{
  "adapted_explanation": "A clear explanation adapted for the {level} level (3-5 sentences)",
  "key_concepts": ["concept1", "concept2", "concept3", "concept4", "concept5"],
  "important_terms": [
    {{"term": "Term1", "definition": "Simple definition"}},
    {{"term": "Term2", "definition": "Simple definition"}},
    {{"term": "Term3", "definition": "Simple definition"}}
  ],
  "real_world_analogy": "A relatable real-world analogy that makes this concept click",
  "example": "A concrete, practical example that demonstrates the concept in action",
  "common_misconception": "The most common mistake or misunderstanding people have about this topic, and why it is wrong",
  "quiz": [
    {{
      "question": "Question 1 appropriate for {level} level?",
      "options": ["A) option", "B) option", "C) option", "D) option"],
      "answer": "A) correct option",
      "explanation": "Brief explanation of why this is correct"
    }},
    {{
      "question": "Question 2 appropriate for {level} level?",
      "options": ["A) option", "B) option", "C) option", "D) option"],
      "answer": "B) correct option",
      "explanation": "Brief explanation of why this is correct"
    }},
    {{
      "question": "Question 3 appropriate for {level} level?",
      "options": ["A) option", "B) option", "C) option", "D) option"],
      "answer": "C) correct option",
      "explanation": "Brief explanation of why this is correct"
    }}
  ]
}}

IMPORTANT: Return ONLY the raw JSON object. No markdown, no code fences, no extra text.

Course Content to Analyze:
{content}"""


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/api/simplify", methods=["POST"])
def simplify():
    data = request.get_json(force=True)
    content = (data.get("content") or "").strip()
    level = (data.get("level") or "Intermediate").strip()

    if not content:
        return jsonify({"error": "Content is required"}), 400
    if level not in ("Beginner", "Intermediate", "Advanced", "Expert"):
        return jsonify({"error": "Invalid proficiency level"}), 400

    try:
        token = get_iam_token()
    except Exception as e:
        return jsonify({"error": f"Authentication failed: {str(e)}"}), 500

    prompt = build_prompt(content, level)

    payload = {
        "model_id": MODEL_ID,
        "project_id": PROJECT_ID,
        "input": prompt,
        "parameters": {
            "decoding_method": "greedy",
            "max_new_tokens": 1800,
            "temperature": 0.3,
            "stop_sequences": [],
        },
    }

    try:
        response = requests.post(
            IBM_URL,
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
            json=payload,
            timeout=60,
        )
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return jsonify({"error": f"IBM API error: {response.text}"}), 502
    except Exception as e:
        return jsonify({"error": f"Request failed: {str(e)}"}), 502

    result = response.json()
    generated_text = result.get("results", [{}])[0].get("generated_text", "").strip()

    # Strip markdown fences if present
    if generated_text.startswith("```"):
        lines = generated_text.split("\n")
        lines = [l for l in lines if not l.startswith("```")]
        generated_text = "\n".join(lines).strip()

    try:
        parsed = json.loads(generated_text)
    except json.JSONDecodeError:
        # Try to extract JSON from the text
        start = generated_text.find("{")
        end = generated_text.rfind("}") + 1
        if start != -1 and end > start:
            try:
                parsed = json.loads(generated_text[start:end])
            except json.JSONDecodeError:
                return jsonify({"error": "Failed to parse model response", "raw": generated_text}), 500
        else:
            return jsonify({"error": "No JSON found in model response", "raw": generated_text}), 500

    return jsonify({"success": True, "level": level, "data": parsed})


@app.route("/api/health")
def health():
    return jsonify({"status": "ok", "service": "LEARNIQ"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
