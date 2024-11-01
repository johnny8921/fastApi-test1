from fastapi import FastAPI, HTTPException, Path, Query, Body, Depends
from typing import Optional, List, Dict, Annotated
from sqlalchemy.orm import Session

from models import Base, User, Post
from database import engine, session_local
from schemas import UserCreate, PostCreate, User as dbUser, PostResponse

app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


@app.post('/users/', response_model=dbUser)
async def create_user(user: UserCreate, db: Session = Depends(get_db)) -> dbUser:
    db_user = User(name=user.name, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.post('/posts/', response_model=PostResponse)
async def create_post(post: PostCreate, db: Session = Depends(get_db)) -> PostResponse:
    db_user: User = db.query(User).filter(User.id == post.author_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail='wrong user id')
    print(db_user)
    db_post = Post(title=post.title, body=post.body, author_id=post.author_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


@app.get('/posts/', response_model=List[PostResponse])
def post_list(db: Session = Depends(get_db)):
    return db.query(Post).all()


@app.get('/users/', response_model=List[dbUser])
def user_list(db: Session = Depends(get_db)):
    return db.query(User).all()

#
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/contacts")
# async def contacts() -> int:
#     return 34
#
#
# @app.get('/items')
# async def items() -> List[Post]:
#     return [Post(**post) for post in posts]
#
#
# @app.post('/items/add')
# async def add_item(post: PostCreate) -> Post:
#     author = next((user for user in users if user['id'] == post.author_id), None)
#     if not author:
#         raise HTTPException(status_code=404, detail="User not found")
#     post_dict = post.dict()
#     post_dict['author'] = author
#     post_dict['id'] = len(posts) + 1
#
#     posts.append(post_dict)
#     print(posts)
#     return Post(**post_dict)
#
#
# @app.get('/items/{id}')
# async def item(id: Annotated[int, Path(..., ge=0, le=100000, title='ID поста')]):
#     for post in posts:
#         if post['id'] == id:
#             return Post(**post)
#     raise HTTPException(status_code=404, detail="Post not found")
#
#
# @app.get('/search')
# async def search(post_id: Annotated[
#     Optional[int],
#     Query(title='id for post search', ge=10000)
# ]) -> Post | Dict[str, Optional[Post]]:
#     if post_id:
#         return await item(post_id)
#     return {"data": None}
#
#
# @app.post('/user/add')
# async def add_user(user: Annotated[
#     UserCreate,
#     Body(..., example=
#     {
#         "name": "userName",
#         "age": "userAge"
#     }
#          )]) -> User:
#     user_dict = user.dict()
#     user_dict['id'] = len(users) + 1
#
#     users.append(user_dict)
#     print(users)
#     return User(**user_dict)
