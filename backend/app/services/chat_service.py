import pandas as pd


class ChatService:

    def __init__(self, dataset_repo):
        self.dataset_repo = dataset_repo

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

        return df