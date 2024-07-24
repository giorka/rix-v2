from domain.interfaces.repositories import AbstractUserRepository
from domain.typevars import User
from infrastructure.datamappers.user import entity_to_model
from infrastructure.gateways.repositories.alchemy.base import AlchemyRepository


class UserRepository(AlchemyRepository, AbstractUserRepository):
    def create(self, entity: User) -> User:
        self.session.add(entity_to_model(entity))

        return entity
