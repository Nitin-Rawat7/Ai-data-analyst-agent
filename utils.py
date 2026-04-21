import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def explain_result(question: str, analysis_result: dict) -> str:
    prompt = f"""
You are an expert data analyst.

You are given:
1. A user's question
2. A computed analysis result from a dataset

Your job is to explain the result clearly, accurately, and professionally.

----------------------------------------
USER QUESTION:
{question}

ANALYSIS RESULT:
{analysis_result}
----------------------------------------

INSTRUCTIONS:

1. Give a direct answer first (1–2 lines).
2. Then explain the result in simple, non-technical language.
3. Highlight key insights or patterns if present.
4. If applicable, mention trends, comparisons, or anomalies.
5. Provide 1–2 actionable recommendations (only if meaningful).
6. Do NOT repeat raw JSON unless necessary.
7. Do NOT make assumptions beyond the given data.
8. If data is insufficient, clearly say so.

----------------------------------------

OUTPUT FORMAT:

Answer:
<clear direct answer>

Insights:
- <insight 1>
- <insight 2>

Explanation:
<simple explanation>

Recommendations:
- <optional recommendation>
- <optional recommendation>

----------------------------------------

Keep the tone professional but easy to understand.
Avoid unnecessary technical jargon.
"""

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )
            return response.text
        except Exception as e:
            if "503" in str(e) or "UNAVAILABLE" in str(e):
                time.sleep(2 * (attempt + 1))
                continue
            return f"Error generating response: {str(e)}"

    return "Model is busy right now. Please try again."