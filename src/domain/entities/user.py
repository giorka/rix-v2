from dataclasses import dataclass

from domain.typealiases import HashedPassword, Password

from . import IEntity


@dataclass
class UserEntity(IEntity):
    username: str
    password: Password | HashedPassword
