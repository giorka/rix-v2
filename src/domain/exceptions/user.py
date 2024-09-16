from dataclasses import dataclass

from . import IException


@dataclass(frozen=True)
class IUserException(IException):
    """Base exception for user exceptions"""

    pass


@dataclass(frozen=True)
class UserAlreadyExistsException(IUserException):
    """Raised when trying to create a user that already exists"""

    username: str

    @property
    def message(self):
        return f'User {self.username} Already Exists'

