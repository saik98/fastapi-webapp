from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.schemas.userschema import UserResponse, UserCreate
from app.services.user_service import get_all_users, create_user
from app.db.session import get_db

router = APIRouter()

@router.get("/", response_model=List[UserResponse])
def read_users(db: Session = Depends(get_db)):
    return get_all_users(db)

@router.post("/", response_model=UserResponse)
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)