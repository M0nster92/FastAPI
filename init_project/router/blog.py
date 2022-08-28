from fastapi import APIRouter, Body
from enum import Enum
from typing import Optional
from pydantic import BaseModel

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

@router.get('/')
def get_all_blogs(page:int, page_size: Optional[int]=None):
    return {'message': f"page {page} & page_size: {page_size}"}

class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"

@router.get('/type/{type}')
def get_blog_type(type: BlogType):
    return {'message': f"blog type: {type}"}

@router.get('/{id}')
def get_blog(id:int):
    return {"message": f"blog id: {id}"}

class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: Optional[int] = Body(..., gt=5, lt=10)


@router.post('/')
def create_blog(blog:BlogModel):
    return "ok"