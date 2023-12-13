from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_users():
    return


@router.post("/")
async def create_user():
    return


@router.get("/{user_id}")
async def get_user(user_id: int):
    return


@router.put("/{user_id}")
async def update_user(user_id: int):
    return


@router.delete("/{user_id}")
async def delete_user(user_id: int):
    return


@router.get("/me")
async def get_me():
    return
