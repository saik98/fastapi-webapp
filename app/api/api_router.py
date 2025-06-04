from fastapi import APIRouter
from app.api.users import router as users_router

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Hello from the FastAPI app"}

# Mount user-related routes
router.include_router(users_router, prefix="/users", tags=["users"])