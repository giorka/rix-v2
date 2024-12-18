import abc

from domain.user.custom_types import *


class IdentityProvider(abc.ABC):
    """
    https://ru.wikipedia.org/wiki/Identity_Provider
    """

    @abc.abstractmethod
    async def get_username(self) -> Username:
        pass
