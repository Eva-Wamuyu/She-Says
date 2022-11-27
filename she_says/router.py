from typing import List
from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .db import sessionLocal, engine,get_db

author = APIRouter(tags=['Authors'],prefix="/api/v1")

@author.get("/authors/",response_model=List[schemas.Author])
def get_authors(skip: int=0, limit: int=20, db: Session=Depends(get_db)):
    authors = crud.get_authors(db,skip=skip,limit=limit)
    return authors

@author.get("/authors/author/{author_id}",response_model=schemas.Author)
def get_author(author_id,db: Session=Depends(get_db)):
    author = crud.get_author(db=db, author_id=author_id)
    if author is None:
        raise HTTPException(status_code=404, detail="author not found")
    return author

 
@author.post("/author",response_model=schemas.AuthorCreate)
def add_author(author:schemas.AuthorBase,db: Session=Depends(get_db)):
    
    return crud.create_author(db=db,author_=author)





book = APIRouter(tags=['Books'],prefix="/api/v1")

@book.get("/books/",response_model=List[schemas.Book])
def get_books(skip: int=0, limit: int=20, db: Session=Depends(get_db)):
    books = crud.get_books(db,skip=skip,limit=limit)
    return books

@book.get("/books/book/{book_id}",response_model=schemas.Book)
def get_book(book_id:int,db: Session=Depends(get_db)):
    book = crud.get_book(db=db,book_id=book_id)
    if book is None:
        raise HTTPException(status_code=400, detail="Book not found")
    return book


@book.post("/book/{author}",response_model=schemas.Book)
def add_book(author:int, book:schemas.BookCreate,db: Session=Depends(get_db)):
    author__ = crud.get_author(db=db,author_id=author)
    if author__ is None:
        raise HTTPException()
    return crud.add_book(db=db, book=book, author_=author)
    
