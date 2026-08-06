import os
import pandas as pd

from app.models.dataset import Dataset
from app.repositories.dataset_repository import DatasetRepository
from app.utils.file_handler import save_upload_file


class DatasetService:

    def __init__(self, repo: DatasetRepository):
        self.repo = repo

    async def upload_dataset(
        self,
        file,
        user_id,
    ):

        stored_name, path = await save_upload_file(file)

        extension = stored_name.split(".")[-1].lower()

        if extension == "csv":
            df = pd.read_csv(path)

        elif extension in ["xlsx", "xls"]:
            df = pd.read_excel(path)

        else:
            raise Exception("Unsupported file type")

        dataset = Dataset(
            user_id=user_id,
            original_name=file.filename,
            stored_name=stored_name,
            storage_path=path,
            file_type=extension,
            file_size=os.path.getsize(path),
            rows=len(df),
            columns=len(df.columns),
            upload_status="completed",
        )

        return await self.repo.create(dataset)
    
    async def get_user_datasets(self, user_id):
        return await self.repo.get_all_by_user(user_id)    