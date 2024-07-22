from domain.entities import UserEntity
from domain.interfaces.repositories import AbstractUserRepository
from infrastructure.datamappers.user import entity_to_model
from infrastructure.gateways.repositories.alchemy.base import AlchemyRepository


class UserRepository(AlchemyRepository, AbstractUserRepository):
    def create(self, entity: UserEntity) -> UserEntity:
        self.session.add(entity_to_model(entity))

        return entity
