from typing import TypeVar

import entities
from interfaces import repositories

User = TypeVar(bound=entities.UserEntity)
UserRepository = TypeVar(bound=repositories.AbstractUserRepository)
