from config import settings
from fastapi import APIRouter, FastAPI

from .users import router as users_router

import uvicorn

routers: list[APIRouter] = [users_router]


def get_application() -> FastAPI:
    application = FastAPI(
        title='RIX',
        description='RIX API',
        docs_url='/api/docs',
        version='dev',
    )
    api_router = APIRouter(prefix='/api')

    for router in routers:
        api_router.include_router(router)

    application.include_router(api_router)

    return application


def get_server(application: FastAPI) -> uvicorn.Server:
    server = uvicorn.Server(uvicorn.Config(app=application, host='0.0.0.0', port=7000, reload=settings.debug))

    return server
