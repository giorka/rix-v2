from adapters.db.base import BaseAlchemyRepository
from adapters.db.models import UserModel
from domain.user.entity import UserEntity
from domain.user.ports.repository import UserRepository

from .datamappers import entity_to_model, model_to_entity

from sqlalchemy.future import select


class UserAlchemyRepositoryImpl(BaseAlchemyRepository, UserRepository):
    async def create(self, entity: UserEntity):
        self._session.add(entity_to_model(entity))

    async def get_by_username(self, username: str) -> UserEntity | None:
        obj = await self._session.scalar(select(UserModel).where(UserModel.username == username))

        if obj is None:
            return None

        return model_to_entity(obj)
