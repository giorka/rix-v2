import abc

from domain.user.custom_types import *

from ..custom_types import *


class TokenProcessor(abc.ABC):
    @abc.abstractmethod
    def make_token(self, username: Username) -> JsonWebTokenData:
        raise NotImplementedError

    @abc.abstractmethod
    async def read_username(self, t: JsonWebToken) -> Username:
        raise NotImplementedError

    @abc.abstractmethod
    async def revoke(self, t: JsonWebToken):
        raise NotImplementedError
