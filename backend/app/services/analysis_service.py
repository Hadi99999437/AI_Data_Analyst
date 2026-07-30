from app.repositories.dataset_repository import DatasetRepository
from app.repositories.analysis_repository import AnalysisRepository

from app.models.analysis_job import AnalysisJob

from app.utils.data_analyzer import (
    load_dataset,
    dataset_summary,
)


class AnalysisService:

    def __init__(
        self,
        dataset_repo: DatasetRepository,
        analysis_repo: AnalysisRepository,
    ):

        self.dataset_repo = dataset_repo
        self.analysis_repo = analysis_repo

    async def analyze_dataset(
        self,
        dataset_id,
        user_id,
    ):

        dataset = await self.dataset_repo.get_by_id(
            dataset_id
        )

        if dataset is None:
            raise Exception("Dataset not found")

        df = load_dataset(
            dataset.storage_path
        )

        summary = dataset_summary(df)

        analysis = AnalysisJob(
            dataset_id=dataset.id,
            user_id=user_id,
            status="completed",
            result_json=summary,
        )

        return await self.analysis_repo.create(
            analysis
        )