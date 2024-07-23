from dataclasses import asdict

from domain.entities import UserEntity
from ..gateways.models import UserModel


def model_to_entity(model: UserModel) -> UserEntity:
    return UserEntity(username=model.username)


def entity_to_model(entity: UserEntity) -> UserModel:
    return UserModel(**asdict(entity))
