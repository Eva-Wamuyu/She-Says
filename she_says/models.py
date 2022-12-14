from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .db import Base


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,index=True)
    bio = Column(String,index=True)

    books = relationship("Book",back_populates="author")


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String,index=True)
    description = Column(String,index=True)
    author_id= Column(Integer,ForeignKey("authors.id"))
    has_cover = Column(Boolean,default=False)
    cover = Column(String)

    author = relationship("Author",back_populates="books")
    