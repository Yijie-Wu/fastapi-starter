import os
from functools import lru_cache

from pydantic_settings import BaseSettings
from pydantic import SecretStr, ConfigDict

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class Settings(BaseSettings):
    title: str = "FastAPI Application"
    version: str = "0.0.1"
    description: str = "A Fastapi Services"
    secret_key: SecretStr
    fastapi_env: str

    model_config = ConfigDict(
        env_file=os.path.join(BASE_DIR, ".env"),
        env_file_encoding="utf-8",
        extra="ignore"  # 可选配置
    )


@lru_cache()
def get_settings():
    return Settings()
