from fastapi import  FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import  models,router
from .db import  engine


app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = "*",
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers = ["*"]
)


@app.get("/")
async def index():
    return {
        "message": "Go to /docs for more information"
    }

models.Base.metadata.create_all(bind=engine)
app.include_router(router.author)
app.include_router(router.book)