from src.dao import BaseDAO
from src.user.models import User


class UserDAO(BaseDAO):
    model = User

    @classmethod
    def me(cls):
        return cls().get(1)
