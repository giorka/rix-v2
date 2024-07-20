from pydantic_settings import BaseSettings as ISettings


class DatabaseSettings(ISettings):
    engine: str
    name: str
    user: str
    password: str
    host: str
    port: str


class ApplicationSettings(ISettings):
    debug: bool = True

    db: DatabaseSettings

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_nested_delimiter = '_'


settings = ApplicationSettings()
