import json
import pandas as pd

from app.models.analysis_job import AnalysisJob
from app.services.insight_service import InsightService
from app.services.ai_service import AIService
from app.services.visualization_service import VisualizationService

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

            # ===========================
            # Load Dataset
            # ===========================

            df = pd.read_csv(dataset.storage_path)

            # ===========================
            # Basic Statistics
            # ===========================

            result = {
                "rows": len(df),
                "columns": len(df.columns),
                "column_names": df.columns.tolist(),
                "data_types": df.dtypes.astype(str).to_dict(),
                "missing_values": df.isnull().sum().to_dict(),
                "duplicate_rows": int(df.duplicated().sum()),
                "summary": df.describe(include="all").fillna("").to_dict(),
            }

            # ===========================
            # Correlation Matrix
            # ===========================

            numeric_df = df.select_dtypes(include="number")

            if len(numeric_df.columns) > 1:

                correlation = (
                    numeric_df
                    .corr()
                    .round(3)
                    .fillna(0)
                    .to_dict()
                )

                result["correlation"] = correlation

            else:

                result["correlation"] = {}

            # ===========================
            # Sample Data
            # ===========================

            result["sample_data"] = (
                df.head(10)
                .fillna("")
                .to_dict(orient="records")
            )

            # ===========================
            # Rule-Based Insights
            # ===========================

            insight_service = InsightService()

            insights = insight_service.generate_insights(result)

            result["rule_based"] = insights

            # ===========================
            # AI Analysis
            # ===========================

            ai_service = AIService()

            ai_prompt = {
                "dataset_information": {
                    "rows": result["rows"],
                    "columns": result["columns"],
                    "column_names": result["column_names"],
                    "data_types": result["data_types"],
                    "missing_values": result["missing_values"],
                    "duplicate_rows": result["duplicate_rows"],
                },
                "summary_statistics": result["summary"],
                "correlation": result["correlation"],
                "sample_data": result["sample_data"],
            }

            ai_result = await ai_service.generate_analysis(
                ai_prompt
            )

            result["ai"] = ai_result

            # ===========================
            # Save Job
            # ===========================

            job.result = result
            job.status = "completed"

            await self.analysis_repo.update(job)

        except Exception as e:

            job.status = "failed"
            job.error_message = str(e)

            await self.analysis_repo.update(job)

        return job