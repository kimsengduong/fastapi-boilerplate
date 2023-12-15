from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.db import Base


class UserAuthentication(Base):
    __tablename__ = "user_authentication"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    password = Column(String(100), nullable=False)
    user = relationship("User", back_populates="authentication")

    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password
