from src.model.requestsModels import Post
from typing import Annotated
from fastapi import FastAPI

app = FastAPI()

@app.post('/api/post')
def createPost(post: Post):
    text = f"The post with title: {post.title} and tags {post.tags} created"
    return text