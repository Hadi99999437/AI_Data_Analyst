import json

from openai import OpenAI

from app.core.config import settings


class AIService:

    def __init__(self):
        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

    async def generate_analysis(
        self,
        analysis_result: dict,
    ):

        prompt = f"""
You are an expert Senior Data Analyst.

Below is the statistical summary of a dataset.

{json.dumps(analysis_result, indent=2)}

Generate a professional report in few sentences.

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

        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert Senior Data Analyst."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            response_format={"type": "json_object"},
        )

        return json.loads(
            response.choices[0].message.content
        )