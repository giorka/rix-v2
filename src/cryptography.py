from typing import TypeVar

from argon2 import PasswordHasher  # noqa

from config import settings

hasher = PasswordHasher()

Content = TypeVar(bound=str)
Response = TypeVar(bound=str)


def encrypt(content: Content) -> Response:
    return hasher.hash(
        content.encode(),
        salt=settings.secret_key
    )


def verify(hashed_string: Response, string: Content) -> bool:
    return hasher.verify(hashed_string, string)
