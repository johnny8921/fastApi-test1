from typing import Optional, List, Dict, Annotated

from fastapi import FastAPI, HTTPException, Path, Query, Body
from pydantic import BaseModel, Field

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


class PostCreate(BaseModel):
    title: str
    body: str
    author_id: int


class UserCreate(BaseModel):
    name: Annotated[
        str, Field(..., title='Имя пользователя', min_length=2, max_length=35)
    ]
    age: Annotated[
        int, Field(..., title='Возраст Пользователя', ge=15, lt=120)
    ]


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


@app.post('/items/add')
async def add_item(post: PostCreate) -> Post:
    author = next((user for user in users if user['id'] == post.author_id), None)
    if not author:
        raise HTTPException(status_code=404, detail="User not found")
    post_dict = post.dict()
    post_dict['author'] = author
    post_dict['id'] = len(posts) + 1

    posts.append(post_dict)
    print(posts)
    return Post(**post_dict)


@app.get('/items/{id}')
async def item(id: Annotated[int, Path(..., ge=0, le=100000, title='ID поста')]):
    for post in posts:
        if post['id'] == id:
            return Post(**post)
    raise HTTPException(status_code=404, detail="Post not found")


@app.get('/search')
async def search(post_id: Annotated[
    Optional[int],
    Query(title='id for post search', ge=10000)
]) -> Post | Dict[str, Optional[Post]]:
    if post_id:
        return await item(post_id)
    return {"data": None}


@app.post('/user/add')
async def add_user(user: Annotated[
    UserCreate,
    Body(..., example=
        {
            "name": "userName",
            "age": "userAge"
        }
    )]) -> User:
    user_dict = user.dict()
    user_dict['id'] = len(users) + 1

    users.append(user_dict)
    print(users)
    return User(**user_dict)