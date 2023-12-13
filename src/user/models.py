from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    authentication = relationship("UserAuthentication", back_populates="user")

    def __init__(self, username, email):
        self.username = username
        self.email = email


class UserAuthentication(Base):
    __tablename__ = "user_authentication"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    password = Column(String(100), nullable=False)
    user = relationship("User", back_populates="authentication")

    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password
