from fastapi import  FastAPI


from fastapi.middleware.cors import CORSMiddleware
from . import  models,router
from .db import  engine


app = FastAPI()







@app.get("/")
async def index():
    return {
        "message": "Go to /docs for more information"
    }

models.Base.metadata.create_all(bind=engine)
app.include_router(router.author)
app.include_router(router.book)
