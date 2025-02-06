from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.modules.authentication.models import UserAuthentication

from app.common.model import Base, BaseModel


class User(BaseModel, UserAuthentication):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    # authentication = relationship("UserAuthentication", back_populates="user")

    # def __init__(self, username, email):
    #     self.username = username
    #     self.email = email
