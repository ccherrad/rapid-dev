from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Date

from core.database import Base


class User(Base):
    __tablename__ = "users"

    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    email = Column(String(254), unique=True, nullable=False)
    password = Column(String(256), nullable=False)
    dob = Column(Date, nullable=True)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    last_login_on = Column(DateTime)
