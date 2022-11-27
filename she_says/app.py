from fastapi import  FastAPI


from . import  models,router
from .db import  engine

models.Base.metadata.create_all(bind=engine)



app = FastAPI()

app.include_router(router.author)
app.include_router(router.book)