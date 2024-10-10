from src.model.requestsModels import Post
from src.controller.mongoConnect import getCollection
from typing import Annotated
from fastapi import FastAPI, Response, status
from datetime import datetime

app = FastAPI()

@app.post('/api/post', status_code=201)
def createPost(post: Post, response: Response):
    collection = getCollection()
    if post.title and post.category and post.content and post.tags:
        result = collection.insert_one({
            'title': post.title,
            'content': post.content,
            'category': post.category,
            'tags': post.tags,
            'createdAt': datetime.now().year,
            'updatedAt': datetime.now().year,
        })
        ack = result.acknowledged
        return {'msg': 'Created'}
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'msg': 'Error'}