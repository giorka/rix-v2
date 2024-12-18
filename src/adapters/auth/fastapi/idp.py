import logging

from domain.auth.ports.idp import IdentityProvider
from domain.user.custom_types import *
from fastapi import Request

from .custom_types import *
from .token_processor import TokenProcessorImpl
from .utils import get_token_from_request

logger = logging.getLogger(__name__)


class FastapiIdentityProviderImpl(IdentityProvider):
    def __init__(self, req: Request, *, token_processor: TokenProcessorImpl):
        self._req = req
        self._token_processor = token_processor

    async def get_username(self) -> Username:
        token = get_token_from_request(self._req)
        logger.debug(f'{token=}')
        username = await self._token_processor.read_username(token)
        logging.debug(f'{username=}')

        return username
