from fastapi import APIRouter

from src.user.api import router as user_router

api_router = APIRouter()

api_router.include_router(
    router=user_router,
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)
