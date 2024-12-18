import logging

from domain.user.custom_types import *
from domain.user.ports.hasher import Hasher
from setup.config import Settings

from argon2 import PasswordHasher
from argon2.exceptions import VerificationError

logger = logging.getLogger(__name__)


class HasherImpl(Hasher):
    def __init__(self, *, hasher: PasswordHasher, settings: Settings):
        self.hasher = hasher
        self.security = settings.security

    def hash(self, password: Password) -> Password:
        return self.hasher.hash(password, salt=self.security.secret.encode())

    def check(self, hashed_password: HashedPassword, password: Password) -> bool:
        logger.debug(f'{hashed_password=} {password=}')

        try:
            self.hasher.verify(hashed_password, password)
        except VerificationError:
            logger.error('Passwords are not equal')
            return False
        else:
            logger.debug('Passwords are equal')
            return True
