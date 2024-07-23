from dataclasses import dataclass

from domain import entities


@dataclass
class UserEntity(entities.IEntity):
    username: str
    password: str
