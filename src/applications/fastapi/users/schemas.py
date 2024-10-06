from domain.typealiases import *

from pydantic import BaseModel as ISchema
from pydantic import Field, field_validator


class RegisterUserRequestSchema(ISchema):
    username: Username = Field(
        min_length=3,
        max_length=32,
        pattern=r'^[a-zA-Z0-9_]+$',
        description=(
            'Username must be between 3 and 32 characters long'
            'and can only contain'
            'letters, numbers, and underscores.'
        ),
        examples=['username'],
    )
    password: Password = Field(min_length=8, max_length=128, examples=['S3cUr3P@$$w0rd'])

    @field_validator('password')  # noqa
    @staticmethod
    def validate_password(password: str) -> str:
        if not 8 <= len(password) <= 128:
            raise ValueError('Password must be between 8 and 128 characters long')
        if not any(char.isupper() for char in password):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(char.islower() for char in password):
            raise ValueError('Password must contain at least one lowercase letter')
        if not any(char.isdigit() for char in password):
            raise ValueError('Password must contain at least one digit')
        if any(char.isspace() for char in password):
            raise ValueError('Password must not contain spaces')

        return password


class LoginUserRequestSchema(ISchema):
    username: Username
    password: Password


class LoginUserResponseSchema(ISchema):
    token: JWT
