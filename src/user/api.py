from fastapi import APIRouter, Depends, HTTPException

from src.authentication import (
    RefreshTokenRequest,
    RefreshTokenResponse,
    SignInRequest,
    SignInResponse,
)
from src.authentication.deps.auth_bearer import JWTBearer, TokenDep
from src.user.commands.refresh_token import RefreshTokenCommand
from src.user.commands.sign_in import SignInCommand
from src.user.commands.sign_up import SignUpCommand
from src.user.dao import UserDAO
from src.user.schemas import UserCreate, UserResponse

router = APIRouter()

DAO = UserDAO()


@router.get("/", dependencies=[TokenDep])
async def get_users(page: int = 1, limit: int = 100):
    return DAO.get_all(
        page=page,
        limit=limit,
    )


@router.post("/")
async def create_user(item: UserCreate, token: str = TokenDep):
    try:
        return SignUpCommand(item).run()

    except HTTPException as e:
        raise e


@router.get("/{user_id}")
async def get_one_user(user_id: int, token: str = TokenDep):
    try:
        return DAO.get(user_id)
    except HTTPException as e:
        raise e


@router.put("/{user_id}", dependencies=[TokenDep])
async def update_user(user_id: int, item_in: dict):
    return DAO.update(user_id, item_in)


@router.delete("/{user_id}", dependencies=[TokenDep])
async def delete_user(user_id: int):
    return DAO.remove(user_id)


@router.get("/me/")
async def read_users_me(token: str = Depends(JWTBearer())):
    try:
        return DAO.me(token)
    except HTTPException as e:
        raise e


@router.post(
    "/sign-in/",
)
async def sign_in(item: SignInRequest) -> SignInResponse:
    try:
        return SignInCommand(item).run()
    except HTTPException as e:
        raise e


@router.post("/sign-up/")
async def sign_up(item: UserCreate) -> UserResponse:
    try:
        return SignUpCommand(item).run()

    except HTTPException as e:
        raise e


@router.post("/refresh-token/")
async def refresh_token(items: RefreshTokenRequest) -> RefreshTokenResponse:
    return RefreshTokenCommand(items).run()
