from dataclasses import asdict

from domain.typevars import User
from ..gateways.models import UserModel


def model_to_entity(model: UserModel) -> User:
    return User(username=model.username, password=model.username)


def entity_to_model(entity: User) -> UserModel:
    return UserModel(**asdict(entity))
