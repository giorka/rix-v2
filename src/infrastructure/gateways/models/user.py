from sqlalchemy import Column, Integer, String

from .base import IModel


class UserModel(IModel):
    id = Column(Integer())
    username = Column(String(length=32), primary_key=True)
