from functools import lru_cache

from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI

from app.core.config import get_settings


@lru_cache
def get_openai_client() -> OpenAI:
    credential = DefaultAzureCredential()
    settings = get_settings()
    base_url = f"https://{settings.azure_openai_endpoint}/openai/v1/"

    token_provider = get_bearer_token_provider(
        credential,
        "https://ai.azure.com/.default",
    )

    client = OpenAI(
        base_url=base_url,
        api_key=token_provider
    )

    return client
