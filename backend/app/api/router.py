from fastapi import APIRouter
from app.api.v1 import report
from app.api.v1 import (
    health,
    auth,
    datasets,
    analysis,
    report
)

api_router = APIRouter()

api_router.include_router(
    health.router,
    prefix="/health",
    tags=["Health"]
)

api_router.include_router(
    auth.router,
    prefix="/auth",
    tags=["Authentication"]
)

api_router.include_router(
    datasets.router
)
api_router.include_router(
    analysis.router,
    prefix="/analysis",
    tags=["Analysis"]
)


api_router.include_router(
    report.router,
    prefix="/report",
    tags=["Report"],
)

