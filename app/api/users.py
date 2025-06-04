from fastapi import APIRouter
from typing import List
from app.models.user import User
from app.services.user_service import get_all_users, create_user

router = APIRouter()

@router.get("/users", response_model=List[User])
def read_users():
    return get_all_users()

@router.post("/users", response_model=User)
def add_user(user: User):
    return create_user(user)