from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
# ST9


class BlogModel(BaseModel):
    title: str
    subtitle: str
    content: str
    author: str
    tags: Optional[List[str]] = []
    date: Optional[datetime] = datetime.now()
    comments: Optional[List[dict]] = []


class UpdateBlogModel(BaseModel):
    title: str = None
    subtitle: str = None
    content: str = None
    author: str = None
    tags: list = None
    comments : list =None


class CommentModel(BaseModel):
    comment_id: str
    content: str
    author: str
    date: Optional[datetime] = datetime.now()
