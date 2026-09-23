from fastapi import APIRouter
from pydantic import BaseModel

from app.api.dependencies import SettingsDep

router = APIRouter()


class HealthResponse(BaseModel):
    status: str = "ok"
    app: str
    environment: str


@router.get("/health", response_model=HealthResponse)
async def health(settings: SettingsDep) -> HealthResponse:
    response = HealthResponse(
        app=settings.app_name,
        environment = settings.environment
    )
    return response
