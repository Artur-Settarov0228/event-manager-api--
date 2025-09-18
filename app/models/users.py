import enum
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text, CheckConstraint, Enum

from app.database import Base


class UserTypes(str, enum.Enum):
    ADMIN = "admin"
    ORGANIZER= "organizer"
    USER = "user"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    full_name = Column(String(100), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    bio = Column(Text, nullable=True)
    user_type = Column(Enum(UserTypes), nullable=False, default=UserTypes.USER)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    __table_args__ = (
        CheckConstraint("LENGTH(username) >= 3", name="username_min_length"),
        CheckConstraint("LENGTH(full_name) >= 3", name="full_name_min_length"),
    )