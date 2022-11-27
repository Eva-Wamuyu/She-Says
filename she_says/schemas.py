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

  
  
class BookView(BookBase):
    id: int
    author_id: int

    class Config:
      orm_mode = True

class Book(BookView):
    id: int
    author_id: int
    author: AuthorBase


class Author(AuthorBase):
    id: int
    books: List[BookView] = []