from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from db import db_article
from schemas import ArticleBase, ArticleDisplay

router = APIRouter(
    prefix='/article',
    tags = ['article']
)

@router.post('/', response_model=ArticleDisplay)
def create_article(req: ArticleBase, db: Session=Depends(get_db)):
    return db_article.create_article(db, req)

@router.get('/{id}', response_model=ArticleDisplay)
def get_article(id: int, db: Session=Depends(get_db)):
    article = db_article.get_article(db, id)
    return article