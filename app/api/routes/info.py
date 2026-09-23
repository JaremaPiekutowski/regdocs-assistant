from fastapi import APIRouter
from pydantic import BaseModel

from app.api.dependencies import SettingsDep

router = APIRouter()


class InfoResponse(BaseModel):
    app_name: str
    environment: str


@router.get("/info", response_model=InfoResponse)
async def info(
    settings: SettingsDep,
) -> InfoResponse:

    response = InfoResponse(
        app_name=settings.app_name,
        environment=settings.environment
    )

    return response
