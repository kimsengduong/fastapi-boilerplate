from typing import Annotated

import colorama
from fastapi import APIRouter, Depends, HTTPException

from src.deps import *
from src.user.dao import UserDAO
from src.user.schemas import UserBase, UserCreate

from src.authentication.deps.auth_bearer import JWTBearer
from src.authentication.auth_handler import decodeJWT, signJWT, decodeJWE

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
    print(colorama.Fore.RED, "item", item, colorama.Style.RESET_ALL)
    return DAO.create(item)


@router.get("/{user_id}")
async def get_one_user(user_id: int, token: TokenDep):
    print(colorama.Fore.RED, "token", token, colorama.Style.RESET_ALL)
    return


@router.put("/{user_id}")
async def update_user(user_id: int, item_in: dict):
    return DAO.update(user_id, item_in)


@router.delete("/{user_id}")
async def delete_user(user_id: int):
    return DAO.remove(user_id)


from src.authentication.auth_handler import decodeJWT, signJWT


@router.get("/sign-in/")
async def sign_in(user_id: int):
    return signJWT(user_id=user_id)


# @router.get("/me/")
# async def get_me(token: TokenDep):
#     print(colorama.Fore.RED, "token", token, colorama.Style.RESET_ALL)
#     return DAO.me()


async def get_current_active_user(
    current_user: Annotated[UserBase, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@router.get("/me/")
async def read_users_me(token: str = Depends(JWTBearer())):
    print(colorama.Fore.RED, "token", decodeJWT(token), colorama.Style.RESET_ALL)
    return {"username": "fakecurrentuser", "email": "", "token": token}


@router.get("/refresh-token/")
async def refresh_token(token: str = Depends(JWTBearer())):
    print(colorama.Fore.RED, "token", decodeJWT(token), colorama.Style.RESET_ALL)
    return {"username": "fakecurrentuser", "email": "", "token": token}
