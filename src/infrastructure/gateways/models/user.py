from .base import IModel

from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped as M
from sqlalchemy.orm import mapped_column


class UserModel(IModel):
    username: M[str] = mapped_column(String(length=32), primary_key=True)
    password: M[str] = mapped_column(String(length=128))
