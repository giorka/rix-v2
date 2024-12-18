import abc

from domain.user.custom_types import *


class AuthProvider(abc.ABC):
    @abc.abstractmethod
    async def login(self, username: Username):
        """
        Raises:
            None
        """
        pass

    @abc.abstractmethod
    async def logout(self):
        """
        Raises:
            None
        """
        pass
