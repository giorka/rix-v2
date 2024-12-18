from abc import ABC, abstractmethod

from ..custom_types import *


class Hasher(ABC):
    @abstractmethod
    def hash(self, password: Password) -> Password:
        pass

    @abstractmethod
    def check(self, hashed_password: HashedPassword, password: Password) -> bool:
        pass
