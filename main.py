from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str

    class Config:
        json_schema_extra = {
            "ejemplo": {
                "title": "hola titulo config",
                "content": "hola content"
            }
        }


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/posts")
def get_posts():
    return {"data": "this is your post"}


@app.get("/post/{id}")
def get_post(id: int):
    return {"data": f"this is your post con id: {id}"}

@app.get("/post")
def get_post(post: Post):
    return post


@app.post("/posts")
def create_post(post: Post):
    return {"data": post}
