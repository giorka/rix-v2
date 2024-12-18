from .base import IModel

from sqlalchemy import String
from sqlalchemy.orm import Mapped as M
from sqlalchemy.orm import mapped_column as Column


class UserModel(IModel):
    username: M[str] = Column(String(length=32), primary_key=True)
    password: M[str] = Column(String(length=128))

    __tablename__ = 'users'
