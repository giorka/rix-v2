from string import ascii_letters, digits

from pydantic import BaseModel as ISchema
from pydantic import Field, field_validator

EXAMPLE_USERNAME = 'giorka'
EXAMPLE_PASSWORD = 'cE2gNI1Fmb2PYoH6'


class RegisterUserSchema(ISchema):
    username: str = Field(examples=[EXAMPLE_USERNAME])
    password: str = Field(examples=[EXAMPLE_PASSWORD])

    @field_validator('username')
    @staticmethod
    def validate_username(username: str) -> str:
        if not 3 <= len(username) <= 32:
            raise ValueError('Username must be between 3 and 32 characters long')
        elif any(char not in (ascii_letters + digits + '_') for char in username):
            raise ValueError('Username can only contain letters, numbers and underscores')

        return username

    @field_validator('password')
    @staticmethod
    def validate_password(password: str) -> str:
        if not 8 <= len(password) <= 128:
            raise ValueError('Password must be between 8 and 128 characters long')
        elif not any(char.isupper() for char in password):
            raise ValueError('Password must contain at least one uppercase letter')
        elif not any(char.islower() for char in password):
            raise ValueError('Password must contain at least one lowercase letter')
        elif not any(char.isdigit() for char in password):
            raise ValueError('Password must contain at least one digit')
        elif any(char.isspace() for char in password):
            raise ValueError('Password must not contain spaces')

        return password


class LoginUserSchema(ISchema):
    username: str = Field(examples=[EXAMPLE_USERNAME])
    password: str = Field(examples=[EXAMPLE_PASSWORD])


class UserSchema(ISchema):
    username: str = Field(examples=[EXAMPLE_USERNAME])
