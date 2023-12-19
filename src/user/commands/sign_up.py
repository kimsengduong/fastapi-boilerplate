from src.authentication import Auth
from src.user.dao import UserDAO
from src.user.schemas import UserCreate
from fastapi import HTTPException


class SignUpCommand:
    def __init__(self, user_create: UserCreate):
        self.user_create = user_create.model_copy()

    def run(self):
        self.validate()

        self.user_create.password = Auth().hash_password(self.user_create.password)

        new_user = UserDAO().create(self.user_create)

        del new_user.password

        return new_user

    def validate(self):
        if UserDAO().get_by_username(self.user_create.username):
            raise HTTPException(400, "Username already exists")
        if UserDAO().get_by_email(self.user_create.email):
            raise HTTPException(400, "Email already exists")
