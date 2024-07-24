from dataclasses import dataclass

from domain import typevars
from domain.entities import UserEntity
from domain.exceptions import UserAlreadyExistsException
from domain.security import encrypt
from domain.uow import AsyncUnitOfWork


@dataclass
class UserService:
    repository: typevars.UserRepository
    uow: AsyncUnitOfWork

    async def register(self, username: str, password: str) -> typevars.User:
        if self.repository.get_by_username(username) is not None:
            raise UserAlreadyExistsException(username)

        hashed_password = encrypt(password)

        entity = UserEntity(username, hashed_password)
        self.repository.create(entity)

        await self.uow.commit()

        return entity
