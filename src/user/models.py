from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.authentication.models import UserAuthentication

from src.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    authentication = relationship("UserAuthentication", back_populates="user")

    # def __init__(self, username, email):
    #     self.username = username
    #     self.email = email
