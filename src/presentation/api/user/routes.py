from domain.auth.errors import *
from domain.auth.ports.aup import AuthProvider
from domain.user.errors import *
from domain.user.interactor import UserInteractor

from ..dependencies import DependsToken
from ..exception_schema import ExceptionSchema
from . import schemas

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, HTTPException, Response
from starlette import status

router = APIRouter(prefix='/user')


@router.post(
    '/register',
    description='Create a new user',
    status_code=201,
    responses={
        status.HTTP_201_CREATED: {'model': schemas.UserSchema},
        status.HTTP_409_CONFLICT: {'model': ExceptionSchema},
    },
)
@inject
async def register(form: schemas.RegisterUserSchema, i: FromDishka[UserInteractor]):
    try:
        user = await i.register(form.username, form.password)
    except UserAlreadyExistsError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)

    return schemas.UserSchema(username=user.username)


@router.post(
    '/login',
    description='Log in as an existing user',
    responses={
        status.HTTP_200_OK: {'model': schemas.UserSchema},
        status.HTTP_401_UNAUTHORIZED: {'model': ExceptionSchema},
    },
)
@inject
async def login(form: schemas.LoginUserSchema, i: FromDishka[UserInteractor]):
    try:
        user = await i.login(form.username, form.password)
    except AuthorizationError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return schemas.UserSchema(username=user.username)


@router.post(
    '/logout',
    description='Log out account',
    dependencies=[DependsToken],
    status_code=status.HTTP_204_NO_CONTENT,
)
@inject
async def logout(i: FromDishka[UserInteractor]):
    await i.logout()


@router.post(
    '/me',
    description='Get your account information',
    responses={
        status.HTTP_200_OK: {'model': schemas.UserSchema},
        status.HTTP_401_UNAUTHORIZED: {'model': ExceptionSchema},
    },
    dependencies=[DependsToken],
)
@inject
async def me(i: FromDishka[UserInteractor]):
    try:
        current_user = await i.get_current_user()
    except AuthenticationError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return schemas.UserSchema(username=current_user.username)
