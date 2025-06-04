from fastapi import APIRouter
from app.api import users  # Assuming you'll create users.py later

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Hello from the FastAPI app"}

# Mount users API
router.include_router(users.router)