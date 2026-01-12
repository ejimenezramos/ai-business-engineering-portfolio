import os
import google.generativeai as genai


def analyze_requirements(requirements_text: str) -> str:
    """
    Analyze business requirements using Gemini.
    """

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not found")

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("models/gemini-flash-latest")

    prompt = f"""
You are a senior software engineer and technical consultant.

Analyze the following business requirements and provide:

1. A list of technical tasks
2. A rough effort estimation
3. Potential risks or ambiguities

Business requirements:
{requirements_text}
"""

    response = model.generate_content(prompt)
    return response.text


if __name__ == "__main__":
    sample_requirements = """
The business needs a web application to allow internal users
to submit reports and track their status.
"""

    result = analyze_requirements(sample_requirements)
    print(result)
