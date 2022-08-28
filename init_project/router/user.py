from typing import List, Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import UserBase, UserDisplay
from db.database import get_db
from db import db_user


router = APIRouter(
    prefix='/user',
    tags=['user']
)

@router.post('/', response_model=UserDisplay)
def create_user(req: UserBase, db: Session= Depends(get_db)):
    return db_user.create_user(db, req)

@router.get('/', response_model=List[UserDisplay])
def get_users(db: Session= Depends(get_db)):
    return db_user.get_all_users(db)

@router.get('/{id}', response_model=Optional[UserDisplay])
def get_user(id: int, db: Session= Depends(get_db)):
    return db_user.get_user(db, id)

@router.post('/{id}/update')
def update_user(id:int, req: UserBase, db: Session= Depends(get_db)):
    return db_user.update_user(db, id, req)

@router.delete('/delete/{id}')
def delete_user(id: int, db: Session= Depends(get_db)):
    return db_user.delete_user(db, id)