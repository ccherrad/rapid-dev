from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from auth.models.user import User
from auth.schemas.user import UserCreate, UserUpdate, UserDelete, UserLogin, UserInDB
from auth.crud.user import create_user, get_user, update_user, delete_user, authenticate
from core.database import get_session

router = APIRouter(tags=["Authentication"], prefix="/auth")

@router.post("/register", response_model=UserInDB)
async def register_user(user: UserCreate, db: Session = Depends(get_session)):
    # Add logic to check if user already exists
    created_user = create_user(db, user.dict())
    return created_user

"""
@router.post("/login")
async def login_user(user_credentials: UserLogin, db: Session = Depends(get_db)):
    user = authenticate(db, user_credentials.email, user_credentials.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    # Add logic for creating JWT token and returning it
    return {"message": "User logged in successfully"}

@router.put("/update_user", response_model=UserInDB)
async def update_user_details(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    updated_user = update_user(db, user_id, user.dict(exclude_unset=True))
    return updated_user

@router.post("/deactivate")
async def deactivate_user(user_id: int, db: Session = Depends(get_db)):
    update_user(db, user_id, {"is_active": False})
    return {"message": "User deactivated successfully"}

@router.delete("/delete")
async def delete_user_account(user_id: int, db: Session = Depends(get_db)):
    if delete_user(db, user_id):
        return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")

@router.get("/get_current_user", response_model=UserInDB)
async def get_current_user(current_user: User = Depends(get_current_active_user)):
    return current_user
"""
