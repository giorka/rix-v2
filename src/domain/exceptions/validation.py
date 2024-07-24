from dataclasses import dataclass

from . import IException


@dataclass(frozen=True)
class IValidationException(IException):
    """Base exception for validation exceptions"""

    pass


@dataclass(frozen=True)
class UserAlreadyExistsException(IValidationException):
    """Raised when trying to create a user that already exists"""

    username: str

    @property
    def message(self):
        return f'User {self.username} Already Exists'
