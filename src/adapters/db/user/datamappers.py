from adapters.db.models import UserModel
from domain.user.entity import UserEntity


def model_to_entity(model: UserModel) -> UserEntity:
    return UserEntity(username=model.username, password=model.password)


def entity_to_model(entity: UserEntity) -> UserModel:
    return UserModel(username=entity.username, password=entity.password)
