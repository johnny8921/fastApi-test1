from typing import Annotated

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    name: Annotated[
        str, Field(..., title='Имя пользователя', min_length=2, max_length=35)
    ]
    age: Annotated[
        int, Field(..., title='Возраст Пользователя', ge=15, lt=120)
    ]


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        from_attributes = True


class PostBase(BaseModel):
    title: str
    body: str
    author_id: int


class PostResponse(PostBase):
    id: int
    author: User

    class Config:
        from_attributes = True


class PostCreate(PostBase):
    pass
