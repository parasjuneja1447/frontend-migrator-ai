# app/agents/analyzer.py

from app.services.gemini_service import analyze_with_gemini
import json
import re

def clean_json(text):
    text = re.sub(r"```json|```", "", text).strip()
    return text

def analyze_sections(sections):
    
    prompt = f"""
You are a frontend expert.

Convert these website sections into UI components.

STRICT RULES:
- Return ONLY valid JSON
- No explanation
- No extra text

Format:
[
  {{
    "component": "Hero",
    "props": {{
      "title": "..."
    }}
  }}
]


Sections:
{sections[:5]}
"""

    response = analyze_with_gemini(prompt)
    response = clean_json(response)

    try:
        return json.loads(response)
    except:
        return {
            "error": "Invalid JSON",
            "raw": response
        }