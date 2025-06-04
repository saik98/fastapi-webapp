from fastapi import FastAPI
from app.api.api_router import router as api_router
from app.db.session import engine
from app.db.base import Base
from app.models import user

app = FastAPI(title="My FastAPI Web Application")

# Create tables
Base.metadata.create_all(bind=engine)

# Include router
app.include_router(api_router)