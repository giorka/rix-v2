from dataclasses import dataclass

from domain.base.error import BaseDomainError

from .custom_types import Username


class BaseUserError(BaseDomainError):
    """Base error for user errors"""

    pass


@dataclass(frozen=True)
class UserAlreadyExistsError(BaseUserError):
    """Raised when trying to create a user that already exists"""

    username: Username

    @property
    def message(self):
        return f'User {self.username} already exists'
