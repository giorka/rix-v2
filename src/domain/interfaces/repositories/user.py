from abc import ABC, abstractmethod

from domain.entities import UserEntity
from domain.typealiases import *

from .base import AbstractRepository


class AbstractUserRepository(AbstractRepository, ABC):
    @abstractmethod
    def create(self, entity: UserEntity) -> UserEntity:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_username(self, username: Username) -> UserEntity:
        raise NotImplementedError()
