import abc

from domain.base.ports.repository import BaseRepository

from ..custom_types import *
from ..entity import UserEntity


class UserRepository(BaseRepository, abc.ABC):
    @abc.abstractmethod
    async def create(self, entity: UserEntity):
        raise NotImplementedError()

    @abc.abstractmethod
    async def get_by_username(self, username: Username) -> UserEntity | None:
        raise NotImplementedError()
