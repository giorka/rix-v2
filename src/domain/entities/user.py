from dataclasses import dataclass

from . import IEntity


@dataclass
class UserEntity(IEntity):
    username: str
    password: str | None = None
