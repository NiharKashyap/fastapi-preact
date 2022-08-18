# build a schema using pydantic
from pydantic import BaseModel
import datetime

class Book(BaseModel):
    title: str
    rating: int
    author_id: int

    class Config:
        orm_mode = True

class Author(BaseModel):
    name:str
    age:int

    class Config:
        orm_mode = True

class UserRequest(BaseModel):
    # id:int
    uname :str
    fname :str
    lname :str
    # date_created: int

    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    id:int
    uname :str
    fname :str
    lname :str
    date_created: datetime.date

    class Config:
        orm_mode = True
