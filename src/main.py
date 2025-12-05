from fastapi import FastAPI
from src.core.config import settings
from src.api.auth import router as auth_router

app = FastAPI(title="Baby Food Catalog")

app.include_router(auth_router)

@app.get("/health")
def health_check():
    return {"status": "ok", "db_url": settings.DATABASE_URL}
