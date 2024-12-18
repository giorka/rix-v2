from dataclasses import dataclass

from domain.base.entity import BaseEntity

from .custom_types import *


@dataclass
class UserEntity(BaseEntity):
    username: Username
    password: HashedPassword
