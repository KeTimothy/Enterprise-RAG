from contextlib import asynccontextmanager

from fastapi import FastAPI


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


@app.get("/")
def root():
    return {"message": "Enterprise RAG is running!"}