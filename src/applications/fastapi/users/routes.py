from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, HTTPException

from domain import exceptions, usecases
from . import schemas

router = APIRouter(prefix='/users')


@router.post(
    '/register',
    description='Create a new user',
    status_code=201,
    responses={
        201: {'model': schemas.LoginUserResponseSchema, 'description': 'Fine!'},
    },
)
@inject
async def register(
        form: schemas.RegisterUserRequestSchema,
        register_user: FromDishka[usecases.RegisterUserUseCase],
):
    try:
        token = await register_user(form.username, form.password)
    except exceptions.UserAlreadyExistsException:
        raise HTTPException(status_code=409, detail='A user with that username already exists.')

    return schemas.LoginUserResponseSchema(token=token)


@router.post(
    '/login',
    description='Log in as an existing user',
    status_code=200,
    responses={
        200: {'model': schemas.LoginUserRequestSchema, 'description': 'Fine!'},
    },
)
@inject
async def login(
        form: schemas.LoginUserRequestSchema,
        login_user: FromDishka[usecases.LoginUserUseCase],
):
    try:
        token = await login_user(form.username, form.password)
    except exceptions.UserDoesNotExistException:
        raise HTTPException(status_code=404, detail='A user with that username does not exists.')
    except exceptions.IncorrectCredentialsException:
        raise HTTPException(status_code=401, detail='Credentials are incorrect.')

    return schemas.LoginUserResponseSchema(token=token)
