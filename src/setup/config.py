import os
from datetime import timedelta
from enum import Enum
from pathlib import Path

from pydantic import PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent


class Algorithm(str, Enum):
    HS256 = 'HS256'
    HS384 = 'HS384'
    HS512 = 'HS512'


class SecuritySettings(BaseSettings):
    secret: str
    algorithm: Algorithm = Algorithm.HS256
    expiration_time: timedelta


class ServerSettings(BaseSettings):
    host: str = '127.0.0.1'
    port: int = 8000


class Settings(BaseSettings):
    is_debug: bool = True

    db: PostgresDsn
    redis: RedisDsn

    server: ServerSettings
    security: SecuritySettings

    class Config:
        env_file = '../.env'
        env_file_encoding = 'utf-8'
        env_nested_delimiter = '.'
