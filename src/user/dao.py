from src.dao import BaseDAO
from src.user.models import User
from src.db import SessionLocal

session = SessionLocal()


class UserDAO(BaseDAO):
    model = User

    @classmethod
    def me(cls):
        return cls().get(1)

    @classmethod
    def get_by_username(cls, username: str) -> User:
        return session.query(cls.model).filter(cls.model.username == username).first()

    @classmethod
    def get_by_email(cls, email: str) -> User:
        return session.query(cls.model).filter(cls.model.email == email).first()
