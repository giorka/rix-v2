from abc import abstractmethod, ABC

from domain.interfaces.repositories import AbstractRepository
from domain.typevars import User


class AbstractUserRepository(AbstractRepository, ABC):
    @abstractmethod
    def create(self, entity: User) -> User:
        raise NotImplementedError()
