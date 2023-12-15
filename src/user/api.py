import colorama
from fastapi import APIRouter

from src.user.dao import UserDAO

router = APIRouter()

DAO = UserDAO()


@router.get("/")
async def get_users(page: int = 1, limit: int = 100):
    return DAO.get_all(
        page=page,
        limit=limit,
    )


@router.post("/")
async def create_user():
    return


@router.get("/{user_id}")
async def get_user(user_id: int, session):
    print(colorama.Fore.RED, "user_id", user_id, colorama.Style.RESET_ALL)
    return


@router.put("/{user_id}")
async def update_user(user_id: int, item_in: dict):
    return DAO.update(user_id, item_in)


@router.delete("/{user_id}")
async def delete_user(user_id: int):
    return DAO.remove(user_id)


@router.get("/me/")
async def get_me():
    return DAO.me()
