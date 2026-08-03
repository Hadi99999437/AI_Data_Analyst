import json
import google.generativeai as genai

from app.core.config import settings


class AIService:

    def __init__(self):

        genai.configure(
            api_key=settings.GEMINI_API_KEY
        )
        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
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

        response = self.model.generate_content(
            prompt
        )

        text = response.text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "")
            text = text.replace("```", "")
            text = text.strip()

        return json.loads(text)