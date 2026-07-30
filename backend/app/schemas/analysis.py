from pydantic import BaseModel


class DatasetSummaryResponse(BaseModel):

    rows: int

    columns: int

    column_names: list[str]

    data_types: dict

    missing_values: dicts