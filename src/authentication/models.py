from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class UserAuthentication:
    password = Column(String(100), nullable=False)
