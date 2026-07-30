import pandas as pd

from app.models.analysis_job import AnalysisJob
from app.repositories.analysis_repository import AnalysisRepository
from app.repositories.dataset_repository import DatasetRepository


class AnalysisService:

    def __init__(
        self,
        analysis_repo: AnalysisRepository,
        dataset_repo: DatasetRepository,
    ):
        self.analysis_repo = analysis_repo
        self.dataset_repo = dataset_repo

    async def analyze_dataset(
        self,
        dataset_id,
        analysis_type,
    ):

        dataset = await self.dataset_repo.get_by_id(dataset_id)

        if dataset is None:
            raise Exception("Dataset not found")

        df = pd.read_csv(dataset.storage_path)

        result = {
            "rows": len(df),
            "columns": len(df.columns),
            "column_names": list(df.columns),
            "missing_values": df.isnull().sum().to_dict(),
            "data_types": df.dtypes.astype(str).to_dict(),
            "summary": df.describe(include="all").fillna("").to_dict(),
        }

        job = AnalysisJob(
            dataset_id=dataset.id,
            analysis_type=analysis_type,
            status="completed",
            result_json=result,
        )

        return await self.analysis_repo.create(job)