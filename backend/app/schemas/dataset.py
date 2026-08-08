from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class DatasetResponse(BaseModel):
    id: UUID
    name: str | None = None
    file_name: str | None = None
    file_type: str | None = None
    file_size: int | None = None
    rows: int | None = None
    columns: int | None = None
    upload_status: str | None = None
    storage_path: str | None = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)