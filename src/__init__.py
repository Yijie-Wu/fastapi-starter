"""
初始化FastAPI
"""
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.config import get_settings, Settings


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title=settings.title,
        version=settings.version,
        description=settings.description,
        lifespan=register_lifespan,
        docs_url=None if settings.fastapi_env == 'production' else '/docs',
        redoc_url=None if settings.fastapi_env == 'production' else '/redoc'
    )

    register_logger(settings, app)
    register_router(settings, app)
    register_database(settings, app)
    register_middlewares(settings, app)

    return app


def register_router(settings: Settings, app: FastAPI):
    pass


def register_logger(settings: Settings, app: FastAPI):
    pass


def register_middlewares(settings: Settings, app: FastAPI):
    pass


def register_database(settings: Settings, app: FastAPI):
    pass


@asynccontextmanager
async def register_lifespan(app: FastAPI):
    print('app start')
    yield
    print('app stop')
