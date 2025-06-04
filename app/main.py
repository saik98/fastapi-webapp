from fastapi import FastAPI
from app.api.routes import router as api_router

app = FastAPI(title="My FastAPI Web Application")

# Register the router
app.include_router(api_router)