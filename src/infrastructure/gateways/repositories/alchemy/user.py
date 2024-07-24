from sqlalchemy.future import select

from domain.interfaces.repositories import AbstractUserRepository
from domain.typevars import User
from infrastructure.datamappers.user import entity_to_model, model_to_entity
from infrastructure.gateways.models import UserModel
from infrastructure.gateways.repositories.alchemy.base import AlchemyRepository


class UserRepository(AlchemyRepository, AbstractUserRepository):
    def create(self, entity: User) -> User:
        self.session.add(entity_to_model(entity))

        return entity

    async def get_by_username(self, username: str) -> User | None:
        response = await self.session.execute(
            select(UserModel)
            .where(User.username == username)
        )
        obj = response.one_or_none()

        if not obj:
            return None

        model = obj[0]

        return model_to_entity(model)
