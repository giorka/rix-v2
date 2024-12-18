from domain.auth.ports.aup import AuthProvider
from domain.user.custom_types import *
from fastapi import Request

from .token_processor import TokenProcessorImpl
from .utils import get_token_from_request


class FastapiAuthProviderImpl(AuthProvider):
    def __init__(self, req: Request, *, token_processor: TokenProcessorImpl):
        self._req = req
        self._token_processor = token_processor

    async def login(self, username: Username):
        token, expires_at = self._token_processor.make_token(username)
        self._req.state.token = (token, expires_at)

    async def logout(self):
        token = get_token_from_request(self._req)

        if token is not None:
            await self._token_processor.revoke(token)
            self._req.state.logout = True
