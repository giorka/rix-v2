from domain.typealiases import *

from pydantic import BaseModel as ISchema


class LoginUserResponseSchema(ISchema):
    token: JWT
