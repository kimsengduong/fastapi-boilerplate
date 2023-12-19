# app/auth/auth_handler.py

import time
from typing import Dict

from jose import jwt, jwe
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from src.config import (
    SECRET_KEY,
    JWT_ALGORITHM,
    JWT_EXP_TIME_MINUTES,
    JWT_REFRESH_EXP_TIME_MINUTES,
)

private_key = rsa.generate_private_key(
    public_exponent=65537, key_size=2048, backend=default_backend()
)
public_key = private_key.public_key()


JWT_SECRET = SECRET_KEY
JWT_ALGORITHM = JWT_ALGORITHM
JWT_EXP = JWT_EXP_TIME_MINUTES
JWT_IAT = time.time()


def signJWT(**kwargs) -> Dict[str, str]:
    # access token
    exp = time.time() + JWT_EXP
    payload = {**kwargs, "exp": exp, "iat": JWT_IAT}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    # refresh token
    refresh_exp = time.time() + JWT_REFRESH_EXP_TIME_MINUTES
    refresh_payload = {**kwargs, exp: refresh_exp, "iat": JWT_IAT}
    refresh_token = jwt.encode(
        refresh_payload,
        JWT_SECRET,
        algorithm=JWT_ALGORITHM,
    )

    jwe_token = jwe.encrypt(
        refresh_token, JWT_SECRET, algorithm="dir", encryption="A128GCM"
    )

    return {
        "access_token": token,
        "expires_in": JWT_EXP * 60,
        "refresh_token": jwe_token,
    }


def decodeJWE(token: str) -> dict:
    try:
        decoded_token = jwe.decrypt(token, JWT_SECRET, algorithms=["dir"])
        return decoded_token if decoded_token["exp"] >= time.time() else None
    except:
        return {}


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["exp"] >= time.time() else None
    except:
        return {}
