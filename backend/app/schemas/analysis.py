from pydantic import BaseModel


class DatasetSummaryResponse(BaseModel):

    rows: int

    columns: int

    column_names: list[str]

    data_types: dict

    missing_values: dict
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class AnalysisRequest(BaseModel):
    dataset_id: UUID
    analysis_type: str


class AnalysisResponse(BaseModel):
    id: UUID
    dataset_id: UUID
    analysis_type: str
    status: str

    model_config = ConfigDict(
        from_attributes=True
    )    