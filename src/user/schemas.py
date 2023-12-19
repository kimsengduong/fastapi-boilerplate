from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=128)


class UserResponse(UserBase):
    id: int

    def __init__(self, **user):
        super().__init__(**user)
