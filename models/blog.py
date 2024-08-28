from pydantic import BaseModel
#ST9 
class BlogModel(BaseModel):
    _id : str
    title : str
    subtitle: str
    content : str
    author: str
    tags: list

class UpdateBlogModel(BaseModel):
    title : str =None
    subtitle: str = None 
    content : str = None
    author: str = None
    tags: list = None