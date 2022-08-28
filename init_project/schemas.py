from typing import List
from pydantic import BaseModel

class UserBase(BaseModel):
    username : str
    email: str
    password: str

class Article(BaseModel):
    title: str
    content : str
    published: bool
    class Config():
        orm_mode = True

class UserDisplay(BaseModel):
    username: str
    email: str
    items : List[Article] = []
    class Config():
        orm_mode = True