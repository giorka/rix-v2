import os
from pathlib import Path

from pydantic_settings import BaseSettings as ISettings

BASE_DIR = Path(__file__).resolve().parent.parent


class DatabaseSettings(ISettings):
    engine: str
    name: str
    user: str
    password: str
    host: str
    port: str

    @property
    def url(self) -> str:
        return '{engine}+asyncpg://{user}:{password}@{host}/{name}'.format(**self.__dict__)


class ApplicationSettings(ISettings):
    debug: bool = True
    secret_key: str = ...

    db: DatabaseSettings

    class Config:
        env_file = os.path.join(BASE_DIR, '.env')
        env_file_encoding = 'utf-8'
        env_nested_delimiter = '_'


settings = ApplicationSettings()
