from dataclasses import dataclass

from domain.typealiases import *

from . import IException


@dataclass(frozen=True)
class IUserException(IException):
    """Base exception for user exceptions"""

    pass


@dataclass(frozen=True)
class UserAlreadyExistsException(IUserException):
    """Raised when trying to create a user that already exists"""

    username: Username

    @property
    def message(self):
        return f'User {self.username} Already Exists'


@dataclass(frozen=True)
class UserDoesNotExistException(IUserException):
    """Raised when trying to create a user that does not exist"""

    username: Username

    @property
    def message(self):
        return f'User {self.username} Does Not Exist'


@dataclass(frozen=True)
class IncorrectCredentialsException(IUserException):
    """Raised when trying to log into a user account when credentials are incorrect"""

    username: Username
    password: Password

    @property
    def message(self):
        return f"{self.username}'s Password Does Not Match {self.password}"
