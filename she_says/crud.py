from sqlalchemy.orm import Session

from . import schemas,models


def get_author(db: Session, author_id:int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()

def get_authors(db: Session, skip: int = 0, limit: int = 20):
    return db.query(models.Author).offset(skip).limit(limit).all()


def create_author(db:Session,author_: schemas.AuthorCreate):
    author = author_.dict()
    print(author)
    new_author = models.Author(
        name = author['name'],
        bio = author['bio'],
    )
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author

def get_books(db:Session,skip: int=0, limit: int=20):
    return db.query(models.Book).offset(skip).limit(limit).all()


def add_book(db:Session, book: schemas.BookCreate, author_:int):
    
    new_book = models.Book(**book.dict(),author_id=author_)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def get_book(db: Session, book_id:int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def get_books_by_author(author_id:int,db:Session,skip: int=0, limit: int=20):
    return db.query(models.Book).filter(models.Book.author_id==author_id).all()