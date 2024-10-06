from dataclasses import dataclass

from domain.typealiases import *

from . import IEntity


@dataclass
class UserEntity(IEntity):
    username: Username
    password: Password | HashedPassword
