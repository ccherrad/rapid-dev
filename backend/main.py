from fastapi import FastAPI

from auth.api import router as auth_router
from core.config import settings
from core.database import SQL_URI

app = FastAPI(
    title="rapid-dev",
)

app.include_router(auth_router)


@app.get("/health")
def health_check():
    return {"status": SQL_URI}
