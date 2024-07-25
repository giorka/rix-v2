from sqlalchemy import Column, String

from .base import IModel


class UserModel(IModel):
    username = Column(String(length=32), primary_key=True)
    password = Column(String(length=128))
