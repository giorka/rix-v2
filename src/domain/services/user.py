from domain import exceptions
from domain.entities import UserEntity
from domain.interfaces.repositories import AbstractUserRepository
from domain.typealiases import *


class UserService:
    def __init__(self, repository: AbstractUserRepository) -> None:
        self._repository = repository

    async def register(self, username: Username, password: Password) -> UserEntity:
        if await self.get_by_username(username) is not None:
            raise exceptions.UserAlreadyExistsException(username)

        entity = UserEntity(username, password)
        self._repository.create(entity)

        return entity

    async def get_by_username(self, username: str) -> UserEntity | None:
        return await self._repository.get_by_username(username)
