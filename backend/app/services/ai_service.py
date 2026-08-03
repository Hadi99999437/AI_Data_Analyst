import json

from google import genai

from app.core.config import settings


class AIService:

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    async def generate_analysis(
        self,
        analysis_result: dict,
    ):

        prompt = f"""
You are an expert Senior Data Analyst.

Below is the statistical summary of a dataset.

{json.dumps(analysis_result, indent=2)}

Generate a professional report.

Return ONLY valid JSON.

Format:

{{
    "summary":"...",
    "insights":[
        "...",
        "...",
        "..."
    ],
    "recommendations":[
        "...",
        "...",
        "..."
    ]
}}
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        text = response.text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "")
            text = text.replace("```", "")
            text = text.strip()

        return json.loads(text)