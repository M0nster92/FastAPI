from http.client import HTTPException
from sqlalchemy.orm.session import Session
from fastapi import HTTPException, status

from db.models import DbArticle
from exception import StoryException
from schemas import ArticleBase

def create_article(db: Session, req: ArticleBase):
    if req.content.startswith('once'):
        raise StoryException('No stories')
    new_article = DbArticle(
        title=req.title,
        content=req.content,
        published = req.published,
        user_id = req.creator_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article

def get_article(db: Session, id: int):
    article = db.query(DbArticle).get(id)
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Article with {id} not found')
    return article