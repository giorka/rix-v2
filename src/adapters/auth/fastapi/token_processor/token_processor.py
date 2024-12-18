import logging
from datetime import datetime, timezone

from domain.auth.errors import AuthenticationError
from domain.user.custom_types import *
from setup.config import Settings

from ..custom_types import *
from .base import TokenProcessor

from jwt import PyJWT
from jwt.exceptions import InvalidTokenError
from redis.asyncio import Redis

logger = logging.getLogger(__name__)


class TokenProcessorImpl(TokenProcessor):
    def __init__(self, *, jwt: PyJWT, r: Redis, settings: Settings):
        self._jwt = jwt
        self._r = r
        self.settings = settings.security

    def make_token(self, username: Username) -> JsonWebTokenData:
        expires_at = datetime.now(tz=timezone.utc) + self.settings.expiration_time
        payload = {'jti': username, 'exp': expires_at}
        token = self._jwt.encode(payload, algorithm=self.settings.algorithm, key=self.settings.secret)

        return (token, expires_at)

    async def read_username(self, t: JsonWebToken) -> Username:
        if await self._r.get(t) is not None:
            logger.info('blacklisted token case')
            raise AuthenticationError

        try:
            return self._jwt.decode(t, algorithms=[self.settings.algorithm], key=self.settings.secret)['jti']
        except InvalidTokenError as err:
            logging.info('misformatted token case')
            raise AuthenticationError from err

    async def revoke(self, t: JsonWebToken):
        async with self._r.pipeline() as p:
            await p.set(t, ' ')
            await p.expire(t, time=self.settings.expiration_time.seconds)

            await p.execute()
