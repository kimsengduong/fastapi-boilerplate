from fastapi import HTTPException

from src.authentication import Auth
from src.dao import BaseDAO
from src.db import SessionLocal
from src.user.models import User

session = SessionLocal()


class UserDAO(BaseDAO):
    model = User

    @classmethod
    def me(cls, token: str) -> User:
        try:
            payload = Auth().decodeJWT(token)
            user_id = payload.get("user_id")
            return cls().get(1)
        except:
            raise HTTPException(401, "Invalid token")

    @classmethod
    def get_by_username(cls, username: str) -> User:
        return session.query(cls.model).filter(cls.model.username == username).first()

    @classmethod
    def get_by_email(cls, email: str) -> User:
        return session.query(cls.model).filter(cls.model.email == email).first()
