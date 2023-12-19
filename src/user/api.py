from typing import Annotated

import colorama
from fastapi import APIRouter, Depends, HTTPException

from src.authentication import (
    RefreshTokenRequest,
    RefreshTokenResponse,
    SignInResponse,
    SignInRequest,
)
from src.authentication.deps.auth_bearer import JWTBearer
from src.deps import *
from src.user.commands.refresh_token import RefreshTokenCommand
from src.user.commands.sign_in import SignInCommand
from src.user.commands.sign_up import SignUpCommand
from src.user.dao import UserDAO
from src.user.schemas import UserBase, UserCreate

router = APIRouter()

DAO = UserDAO()


@router.get("/")
async def get_users(page: int = 1, limit: int = 100):
    return DAO.get_all(
        page=page,
        limit=limit,
    )


@router.post("/")
async def create_user(item: UserCreate):
    return DAO.create(item)


@router.get("/{user_id}")
async def get_one_user(user_id: int, token: TokenDep):
    return


@router.put("/{user_id}")
async def update_user(user_id: int, item_in: dict):
    return DAO.update(user_id, item_in)


@router.delete("/{user_id}")
async def delete_user(user_id: int):
    return DAO.remove(user_id)


@router.post("/sign-in/")
async def sign_in(item: SignInRequest) -> SignInResponse:
    return SignInCommand(item).run()


@router.post("/sign-up/")
async def sign_up(item: UserCreate):
    return SignUpCommand(item).run()


# @router.get("/me/")
# async def get_me(token: TokenDep):
#     return DAO.me()


async def get_current_active_user(
    current_user: Annotated[UserBase, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@router.get("/me/")
async def read_users_me(token: str = Depends(JWTBearer())):
    return {"username": "fakecurrentuser", "email": "", "token": token}


@router.post("/refresh-token/")
async def refresh_token(items: RefreshTokenRequest) -> RefreshTokenResponse:
    return RefreshTokenCommand(items).run()
