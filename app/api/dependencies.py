from typing import Annotated

from fastapi import Depends
from openai import OpenAI

from app.core.config import Settings, get_settings
from app.infrastructure.azure_openai import get_openai_client

SettingsDep = Annotated[Settings, Depends(get_settings)]
OpenAIClientDep = Annotated[OpenAI, Depends(get_openai_client)]
