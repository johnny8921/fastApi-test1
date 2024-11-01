from typing import Optional

from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/contacts")
async def contacts() -> int:
    return 34


posts = [
    {
        "id": 1,
        "title": "title of post 1",
        "body": "body of post 1",

    },
    {
        "id": 2,
        "title": "title of post 2",
        "body": "body of post 2",

    },
    {
        "id": 3,
        "title": "title of post 3",
        "body": "body of post 3",

    }
]


@app.get('/items')
async def items() -> list[dict]:
    return posts


@app.get('/items/{id}')
async def item(id: int) -> dict:
    for post in posts:
        if post['id'] == id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")


@app.get('/search')
async def search(post_id: Optional[int]) -> dict:
    if post_id:
        return await item(post_id)
    return {"message": "Post not found"}
