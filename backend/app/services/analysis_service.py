import pandas as pd

from app.models.analysis_job import AnalysisJob
from app.services.insight_service import InsightService
from app.services.ai_service import AIService


class AnalysisService:

    def __init__(
        self,
        dataset_repo,
        analysis_repo,
    ):
        self.dataset_repo = dataset_repo
        self.analysis_repo = analysis_repo

    async def run_analysis(
        self,
        dataset_id,
        analysis_type,
        user_id,
    ):

        dataset = await self.dataset_repo.get_by_id(
            dataset_id
        )

        if dataset is None:
            raise Exception("Dataset not found")

        job = AnalysisJob(
            dataset_id=dataset.id,
            analysis_type=analysis_type,
            status="running",
        )

        job = await self.analysis_repo.create(job)

        try:

            df = pd.read_csv(dataset.storage_path)

            result = {
                "rows": len(df),
                "columns": len(df.columns),
                "column_names": df.columns.tolist(),
                "missing_values": df.isnull().sum().to_dict(),
                "summary": df.describe(include="all").fillna("").to_dict(),
            }

            # Rule-based insights
            insight_service = InsightService()

            insights = insight_service.generate_insights(result)

            result["insights"] = insights["insights"]
            result["recommendations"] = insights["recommendations"]

            # -------------------------------
            # AI Generated Insights (Gemini)
            # -------------------------------

            ai_service = AIService()

            ai_result = await ai_service.generate_analysis(result)

            result["ai"] = {
                "summary": ai_result["summary"],
                "insights": ai_result["insights"],
                "recommendations": ai_result["recommendations"],
            }

            job.result = result
            job.status = "completed"

            await self.analysis_repo.update(job)

        except Exception as e:

            job.status = "failed"
            job.error_message = str(e)

            await self.analysis_repo.update(job)

        return job