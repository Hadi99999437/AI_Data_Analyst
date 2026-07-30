from sqlalchemy.orm import DeclarativeBase
from app.models.user import User
from app.models.dataset import Dataset
from app.models.analysis_job import AnalysisJob

class Base(DeclarativeBase):
    pass