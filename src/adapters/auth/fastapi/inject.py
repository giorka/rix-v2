import logging

from fastapi import FastAPI, Request, Response

from .custom_types import *
from .utils import delete_cookie_from_response, set_token_to_response

logger = logging.getLogger(__name__)


def inject_auth(app: FastAPI):
    @app.middleware('http')
    async def AuthMiddleware(req: Request, call_next) -> Response:
        resp: Response = await call_next(req)

        token_data: JsonWebTokenData | None = getattr(req.state, 'token', None)

        if token_data:
            token, expires_at = token_data
            set_token_to_response(resp, token=token, expires=expires_at)

        is_logout = getattr(req.state, 'logout', False)

        if is_logout is True:
            delete_cookie_from_response(resp)

        return resp

    return app
