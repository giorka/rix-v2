from sqlalchemy import Column, Integer

from .base import IModel


class UserModel(IModel):
    id = Column(Integer(), primary_key=True)
