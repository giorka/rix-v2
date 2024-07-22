from abc import abstractmethod, ABC

from domain.entities import UserEntity
from domain.interfaces.repositories import AbstractRepository


class AbstractUserRepository(AbstractRepository, ABC):
    @abstractmethod
    def create(self, entity: UserEntity) -> UserEntity:
        ...
