import logging

from domain.base.service import BaseService

from .custom_types import *
from .entity import UserEntity
from .ports.hasher import Hasher

logger = logging.getLogger(__name__)


class UserService(BaseService):
    def __init__(self, h: Hasher):
        self._hasher = h

    def create_user(self, username: Username, password: Password) -> UserEntity:
        hashed_password = self._hasher.hash(password)
        return UserEntity(username, hashed_password)

    def check_password(self, user: UserEntity, password: Password) -> bool:
        return self._hasher.check(hashed_password=user.password, password=password)
