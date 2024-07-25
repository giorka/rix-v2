from dataclasses import dataclass

from domain.entities import UserEntity
from domain.exceptions import UserAlreadyExistsException
from domain.interfaces.repositories import AbstractUserRepository
from domain.security import encrypt
from domain.uow import AsyncUnitOfWork


@dataclass
class UserService:
    # TODO: rename to _repository, _uow
    repository: AbstractUserRepository
    uow: AsyncUnitOfWork

    async def register(self, username: str, password: str) -> UserEntity:
        if await self.repository.get_by_username(username) is not None:
            raise UserAlreadyExistsException(username)

        hashed_password = encrypt(password)

        entity = UserEntity(username, hashed_password)
        self.repository.create(entity)

        await self.uow.commit()

        return entity

    async def get_by_username(self, username: str) -> UserEntity | None:
        return await self.repository.get_by_username(username)
