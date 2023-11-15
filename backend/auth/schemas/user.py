from typing import Optional
from datetime import date, datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    dob: date


class UserRegister(UserBase):
    password: str
    name: Optional[str]
