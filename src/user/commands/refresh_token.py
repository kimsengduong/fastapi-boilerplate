from src.authentication import Auth, RefreshTokenRequest, RefreshTokenResponse


class RefreshTokenCommand:
    def __init__(self, items: RefreshTokenRequest):
        self.refresh_token = items.refresh_token
        self.decoded_token = None

    def run(self) -> RefreshTokenResponse:
        self.validate()

        return RefreshTokenResponse(
            **Auth().signJWT(user_id=self.decoded_token["user_id"])
        )

    def validate(self):
        decrypted_token = Auth().decodeRefreshJWE(self.refresh_token)
        if not decrypted_token:
            raise Exception("Invalid token")

        self.decoded_token = Auth().decodeRefreshJWT(decrypted_token)
        if not self.decoded_token:
            raise Exception("Token expired")
