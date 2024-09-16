from argon2 import PasswordHasher  # noqa

from config import settings
from .base import Password, HashedPassword

hasher = PasswordHasher()


def make_password(password: Password) -> HashedPassword:
    return hasher.hash(password.encode(), salt=settings.hashing_secret.encode())


def check_password(hashed_password: HashedPassword, password: Password) -> bool:
    return hasher.verify(hashed_password, password)
