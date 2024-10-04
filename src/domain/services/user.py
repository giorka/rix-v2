from dataclasses import dataclass
from domain import exceptions
from domain.entities import UserEntity
from domain.interfaces.repositories import AbstractUserRepository
from domain.security import encrypt
from domain.uow import AsyncUnitOfWork


@dataclass
class UserService:
    _repository: AbstractUserRepository
    _uow: AsyncUnitOfWork

    async def register(self, username: str, password: str) -> UserEntity:
        if await self.get_by_username(username) is not None:
            raise exceptions.UserAlreadyExistsException(username)

        hashed_password = encrypt(password)

        entity = UserEntity(username, hashed_password)
        self._repository.create(entity)

        await self._uow.commit()

        return entity

    async def get_by_username(self, username: str) -> UserEntity | None:
        return await self._repository.get_by_username(username)
