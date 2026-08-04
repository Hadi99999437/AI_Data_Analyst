from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings
from app.routers import chat
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)


@app.get("/")
async def root():
    return {
        "message": "AI Data Analyst API is running 🚀"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }


app.include_router(
    api_router,
    prefix="/api/v1"
)

app.include_router(
    chat.router,
    prefix="/api/v1/chat",
    tags=["Chat"]
)