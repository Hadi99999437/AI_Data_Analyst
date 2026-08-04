import pandas as pd

from app.services.ai_service import AIService


class ChatService:

    def __init__(self, dataset_repo):

        self.dataset_repo = dataset_repo

        self.ai_service = AIService()

    async def ask_question(
        self,
        dataset_id,
        question,
    ):

        dataset = await self.dataset_repo.get_by_id(
            dataset_id
        )

        if dataset is None:
            raise Exception("Dataset not found")

        df = pd.read_csv(
            dataset.storage_path
        )

        prompt = f"""
You are an expert Data Analyst.

Dataset Information

Rows:
{len(df)}

Columns:
{df.columns.tolist()}

Data Types:
{df.dtypes.astype(str).to_dict()}

Missing Values:
{df.isnull().sum().to_dict()}

Summary Statistics:
{df.describe(include='all').fillna('').to_string()}

Sample Data:
{df.head(20).to_markdown(index=False)}

User Question:
{question}

Answer professionally in few sentences .
"""

        answer = await self.ai_service.generate_chat_response(
            prompt
        )

        return answer