from fastapi import FastAPI
from src.core.config import settings


app = FastAPI(title="Baby Food Catalog")


@app.get("/health")
def health_check():
    return {"status": "ok", "db_url": settings.DATABASE_URL}
