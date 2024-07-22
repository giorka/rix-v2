from sqlalchemy import Column, Integer, String

from .base import IModel


class UserModel(IModel):
    id = Column(Integer(), primary_key=True)
    username = Column(String(length=32))
