from typing import Optional, List, Dict

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/contacts")
async def contacts() -> int:
    return 34


class User(BaseModel):
    id: int
    name: str
    age: int


class Post(BaseModel):
    id: int
    title: str
    body: str
    author: User


users = [
    {'id': 1, 'name': 'John Doe', 'age': 30},
    {'id': 2, 'name': 'Диана', 'age': 25},
    {'id': 3, 'name': 'Bob Smith', 'age': 40},
]

posts = [
    {
        "id": 1,
        "title": "title of post 1",
        "body": "body of post 1",
        'author': users[1]

    },
    {
        "id": 2,
        "title": "title of post 2",
        "body": "body of post 2",
        'author': users[2]

    },
    {
        "id": 3,
        "title": "title of post 3",
        "body": "body of post 3",
        'author': users[0]

    }
]


@app.get('/items')
async def items() -> List[Post]:
    return [Post(**post) for post in posts]


@app.get('/items/{id}')
async def item(id: int) -> Post:
    for post in posts:
        if post['id'] == id:
            return Post(**post)
    raise HTTPException(status_code=404, detail="Post not found")


@app.get('/search')
async def search(post_id: Optional[int]) -> Post | Dict[str, Optional[Post]]:
    if post_id:
        return await item(post_id)
    return {"data": None}
