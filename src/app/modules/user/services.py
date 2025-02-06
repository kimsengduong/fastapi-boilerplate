import logging
from typing import List, Optional

from fastapi import HTTPException
from passlib.context import CryptContext

from app.modules.authentication.auth import Auth
from app.modules.authentication.schemas import (
    RefreshTokenRequest,
    RefreshTokenResponse,
    SignInRequest,
    SignInResponse,
)
from app.modules.user.models import User
from app.modules.user.repository import UserRepository
from app.modules.user.schemas import UserCreate, UserResponse, UserUpdate

logger = logging.getLogger(__name__)


class UserService:
    def __init__(self):
        self.repository = UserRepository()
        self.auth = Auth()

    async def create_user(self, user_in: UserCreate) -> User:
        """Create new user with hashed password"""
        # Check if email exists - add await
        if await self.repository.get_by_email(user_in.email):
            raise ValueError("Email already registered")

        # Check if username exists - add await
        if await self.repository.get_by_username(user_in.username):
            raise ValueError("Username already registered")

        # Hash the password
        hashed_password = self.auth.hash_password(user_in.password)

        # Create user object
        user = UserCreate(
            email=user_in.email,
            username=user_in.username,
            password=hashed_password,
        )

        # Save and return the created user - add await
        created_user = await self.repository.create(user)
        return created_user

    async def authenticate(self, identifier: str, password: str) -> Optional[User]:
        """Authenticate user by email or username and password"""
        user = await self.repository.get_by_email(
            identifier
        ) or await self.repository.get_by_username(identifier)

        if not user or not self.auth.verify_password(password, user.password):
            return None
        return user

    async def get_user(self, user_id: int) -> Optional[User]:
        """Get user by ID"""
        user = await self.repository.get(user_id)

        return UserResponse(**user.__dict__) if user else None

    async def update_user(self, user_id: int, user_in: UserUpdate) -> User:
        """Update user profile"""
        current_user = self.repository.get(user_id)
        if not current_user:
            raise ValueError("User not found")

        return await self.repository.update(current_user, user_in)

    async def get_active_users(
        self, offset: int = 0, limit: int = 100
    ) -> List[UserResponse]:
        """Get list of active users"""
        users = await self.repository.get_active_users(offset=offset, limit=limit)
        return [UserResponse(**user.__dict__) for user in users]

    # Authentication related functions
    async def sign_in(self, credentials: SignInRequest) -> SignInResponse:
        """
        Authenticate user and generate JWT token
        """
        user = await self.authenticate(credentials.username, credentials.password)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid credentials")

        return SignInResponse(**self.auth.signJWT(user_id=user.id, email=user.email))

    async def sign_up(self, user_in: UserCreate) -> SignInResponse:
        """
        Register new user and return JWT token
        """
        try:
            user = await self.create_user(user_in)
            logger.info(f"User created: {user}")
            return SignInResponse(
                **self.auth.signJWT(user_id=user.id, email=user.email)
            )
        except ValueError as e:
            logger.error(f"Error signing up user: {e}")
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            logger.error(f"Error signing up user: {e}")
            raise HTTPException(status_code=500, detail=str(e))

    async def refresh_token(self, request: RefreshTokenRequest) -> RefreshTokenResponse:
        """
        Refresh access token using refresh token
        """
        try:
            # Decrypt JWE token
            decrypted_token = self.auth.decodeRefreshJWE(request.refresh_token)
            if not decrypted_token:
                raise HTTPException(status_code=401, detail="Invalid token")

            # Decode JWT claims
            decoded_token = self.auth.decodeRefreshJWT(decrypted_token)
            if not decoded_token:
                raise HTTPException(status_code=401, detail="Token expired")

            # Generate new token pair
            return RefreshTokenResponse(
                **self.auth.signJWT(user_id=decoded_token["user_id"])
            )
        except Exception as e:
            logger.error(f"Error refreshing token: {e}")
            raise HTTPException(status_code=401, detail=str(e))

    async def get_me(self, token: str) -> User:
        """
        Get current user details from token
        """
        try:
            decoded_token = self.auth.decodeJWT(token)
            if not decoded_token:
                raise HTTPException(status_code=401, detail="Invalid token")

            user = await self.get_user(decoded_token["user_id"])
            if not user:
                raise HTTPException(status_code=404, detail="User not found")

            return user
        except Exception as e:
            logger.error(f"Error getting user: {e}")
            raise HTTPException(status_code=401, detail=str(e))
