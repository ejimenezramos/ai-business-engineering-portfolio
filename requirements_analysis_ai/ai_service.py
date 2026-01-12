import os
import google.generativeai as genai


def analyze_requirements(requirements_text: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not found")

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("models/gemini-flash-latest")

    prompt = f"""
You are a senior software engineer and technical consultant.

Analyze the following business requirements and return the result
STRICTLY in Markdown using the following structure:

## Technical Tasks
- Bullet list of concrete technical tasks

## Estimation
- Rough effort estimation (days or weeks)
- Assumptions if needed

## Risks and Ambiguities
- Bullet list of potential risks, unclear points or missing information

Business requirements:
{requirements_text}
"""

    response = model.generate_content(prompt)
    return response.text

def split_analysis_sections(text: str) -> dict:
    sections = {
        "tasks": "",
        "estimation": "",
        "risks": ""
    }

    current_section = None

    for line in text.splitlines():
        line_lower = line.lower()

        if line_lower.startswith("## technical tasks"):
            current_section = "tasks"
            continue
        elif line_lower.startswith("## estimation"):
            current_section = "estimation"
            continue
        elif line_lower.startswith("## risks"):
            current_section = "risks"
            continue

        if current_section:
            sections[current_section] += line + "\n"

    return sections

