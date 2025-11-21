# src/models/__init__.py
from src.database import Base

# Также здесь можно импортировать все модели, чтобы Alembic их увидел:
from src.models.user import User

__all__ = ["Base", "User"]
