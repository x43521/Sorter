from sqlalchemy import Column, Integer, String, Index
from src.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    __table_args__ = (Index("ix_users_email_unique", "email", unique=True),)
