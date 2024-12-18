from adapters.auth.fastapi.inject import inject_auth
from presentation.api import routers
from setup.config import Settings

from .providers import *

from dishka import AsyncContainer, make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import APIRouter, FastAPI


def get_container(settings: Settings) -> AsyncContainer:
    return make_async_container(
        AuthDependencyProvider(),
        UserDependencyProvider(),
        DatabaseDependencyProvider(),
        SettingsProvider(),
        context={Settings: settings},
    )


def setup_routers(app: FastAPI) -> FastAPI:
    api_router = APIRouter(prefix='/api')

    for router in routers:
        api_router.include_router(router)

    app.include_router(api_router)

    return app


def get_app(container: AsyncContainer) -> FastAPI:
    app = FastAPI(title='RIX', description='RIX API', docs_url='/api/docs', version='dev')
    setup_routers(app)

    setup_dishka(container, app=app)

    inject_auth(app)

    return app
