from typing import TypeVar

Password = TypeVar('Password', bound=str)
HashedPassword = TypeVar('HashedPassword', bound=str)
Token = TypeVar('Token', bound=str)
