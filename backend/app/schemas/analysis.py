from pydantic import BaseModel


class DatasetSummaryResponse(BaseModel):

    rows: int

    columns: int

    column_names: list[str]

    data_types: dict

    missing_values: dict
from uuid import UUID
from typing import Optional, Dict, Any

from pydantic import BaseModel


class AnalysisRequest(BaseModel):
    dataset_id: UUID
    analysis_type: str


class AnalysisResponse(BaseModel):
    id: UUID
    dataset_id: UUID
    analysis_type: str
    status: str

    result: Optional[Dict[str, Any]] = None
    error_message: Optional[str] = None

    model_config = {
        "from_attributes": True
    }