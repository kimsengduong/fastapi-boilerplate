from src.authentication import (
    Auth,
    SignInRequest,
    SignInResponse,
)
from src.user.dao import UserDAO
from src.user.models import User


class SignInCommand:
    def __init__(self, credential: SignInRequest):
        self.credential = credential
        self.user: User = None

    def run(self) -> SignInResponse:
        self.validate()

        return SignInResponse(
            **Auth().signJWT(user_id=self.user.id, email=self.user.email)
        )

    def validate(self):
        self.user = UserDAO().get_by_username(self.credential.username)
        if not self.user:
            raise Exception("User not found")
        if not Auth().verify_password(self.credential.password, self.user.password):
            raise Exception("Wrong password")
