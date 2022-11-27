from typing import Union,List

from pydantic import BaseModel


class AuthorBase(BaseModel):
    name: str
    bio: Union[str,None ] = None


    class Config:
        orm_mode = True

class AuthorCreate(AuthorBase):
    pass

class BookBase(BaseModel):
    title: str
    description: Union[str,None ] = None

class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int
    author_id: int
    author: AuthorBase

    class Config:
        orm_mode = True

class Author(AuthorBase):
    id: int
    books: List[Book] = []