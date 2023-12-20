from fastapi import APIRouter

from src.user.api import router as user_router
from .config import APP_NAME, APP_VERSION, APP_CONTACT

api_router = APIRouter()


@api_router.get("/")
async def root():
    return {"name": APP_NAME, "version": APP_VERSION, "contact": APP_CONTACT}


api_router.include_router(
    router=user_router,
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)
