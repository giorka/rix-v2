from domain.entities import UserEntity
from domain.interfaces.repositories import AbstractUserRepository
from infrastructure.datamappers.user import entity_to_model, model_to_entity
from infrastructure.gateways.models import UserModel
from infrastructure.gateways.repositories.alchemy import AlchemyRepository

from sqlalchemy.future import select


class UserRepository(AlchemyRepository, AbstractUserRepository):
    def create(self, entity: UserEntity) -> UserEntity:
        self.session.add(entity_to_model(entity))

        return entity

    async def get_by_username(self, username: str) -> UserEntity | None:
        obj = await self.session.scalar(select(UserModel).where(UserModel.username == username))

        if obj is None:
            return None

        return model_to_entity(obj)
