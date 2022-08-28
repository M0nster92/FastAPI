from sqlalchemy.orm.session import Session
from fastapi import HTTPException, status

from db.hash import Hash
from schemas import UserBase
from db.models import DbUser

def create_user(db: Session, req: UserBase):
    new_user = DbUser(
    username = req.username,
    email = req.email,
    password = Hash.bcrypt(req.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db: Session):
    return db.query(DbUser).all()

def get_user(db: Session, id: int):
    user = db.query(DbUser).get(id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with {id} is not found")
    return user

def update_user(db: Session, id: int, req: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with {id} is not found")
    user.update({
        DbUser.username: req.username,
        DbUser.email: req.email,
        DbUser.password: Hash.bcrypt(req.password)
    })
    db.commit()
    return 'ok'

def delete_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with {id} is not found")
    db.delete(user)
    db.commit()
    return 'ok'