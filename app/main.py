from contextlib import asynccontextmanager

from fastapi import FastAPI

from sqlalchemy import text
from app.db.database import engine
from app.api.routes.documents import router as documents_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application starting")
    yield
    print("Application shutting down")


app = FastAPI(
    title="Enterprise RAG",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(documents_router)

@app.get("/")
def root():
    return {"message": "Enterprise RAG is running!"}


@app.get("/health/db")
def health_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        return {"result": result.scalar()}