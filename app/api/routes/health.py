from typing import Annotated, Any

from fastapi import APIRouter, Depends

from app.core.config import Settings, get_settings

router = APIRouter()

SettingsDep = Annotated[Settings, Depends(get_settings)]


@router.get("/health")
async def health(settings: SettingsDep) -> dict[str, Any]:
    return {
        "status": "ok",
        "app": settings.app_name,
        "environment": settings.environment
    }
