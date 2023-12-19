from pydantic import BaseModel


class SignInRequest(BaseModel):
    username: str
    password: str


class SignInResponse(BaseModel):
    access_token: str
    expires_in: int
    refresh_token: str


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class RefreshTokenResponse(BaseModel):
    access_token: str
    expires_in: int
