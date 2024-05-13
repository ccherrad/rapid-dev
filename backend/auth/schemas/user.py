from pydantic import BaseModel, EmailStr

# User Base Schema
class UserBase(BaseModel):
    email: EmailStr

# Schema for User Creation
class UserCreate(UserBase):
    password: str

# Schema for User Update
class UserUpdate(BaseModel):
    email: EmailStr = None
    is_active: bool = None

# Schema for User Deletion
class UserDelete(BaseModel):
    user_id: int

# Schema for User Login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Schema for User in Response
class UserInDB(UserBase):
    id: int
    is_active: bool
    is_superuser: bool

    class Config:
        from_attributes = True
