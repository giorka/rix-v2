from abc import abstractmethod, ABC

from domain.entities import UserEntity
from .base import AbstractRepository


class AbstractUserRepository(AbstractRepository, ABC):
    @abstractmethod
    def create(self, entity: UserEntity) -> UserEntity:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_username(self, username: str) -> UserEntity:
        raise NotImplementedError()
