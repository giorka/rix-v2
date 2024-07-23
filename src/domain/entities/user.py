from domain import entities, fields


class UserCredentialsEntity(entities.IEntity):
    username: fields.username
    password: str


class UserEntity(entities.IEntity):
    username: fields.username
