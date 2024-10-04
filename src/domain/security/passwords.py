import argon2  # noqa

from config import settings
from domain.typealiases import *

hasher = argon2.PasswordHasher()


def make_password(password: Password) -> HashedPassword:
    return hasher.hash(password.encode(), salt=settings.hashing_secret.encode())


def check_password(hashed_password: HashedPassword, password: Password) -> bool:
    try:
        hasher.verify(hashed_password, password)
    except argon2.exceptions.VerifyMismatchError:
        return False
    else:
        return True
