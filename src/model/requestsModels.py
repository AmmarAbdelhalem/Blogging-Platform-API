from pydantic import BaseModel

class Post(BaseModel):
    title: str
    content: str
    category: str
    tags: list[str]