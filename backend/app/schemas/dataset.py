from uuid import UUID

from pydantic import BaseModel, ConfigDict


class DatasetResponse(BaseModel):

    id: UUID

    original_name: str

    stored_name: str

    file_type: str

    rows: int

    columns: int

    upload_status: str

    model_config = ConfigDict(
        from_attributes=True
    )