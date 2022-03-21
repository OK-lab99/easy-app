from sqlalchemy.orm import Session
import models
import schemas
from fastapi.encoders import jsonable_encoder
from typing import List
from fastapi import HTTPException
from typing import Any, Dict, Optional, Union

from utils.auth_utils import get_password_hash, verify_password
from typing import Optional


#emailからuser取得
def get_by_email(db: Session, email: str) -> models.User:
        return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_username(db: Session, username: str):
    user = db.query(models.User).filter(models.User.name == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with id {user} not found')
    return user

def create_user(db: Session, user: schemas.UserCreate) -> models.User:
     db_obj = models.User(name=user.name, email=user.email, hashed_password=get_password_hash(user.password))
     db.add(db_obj)
     db.commit()
     db.refresh(db_obj)
     return db_obj

def is_active(user: schemas.User) -> bool:
     return user.is_active

def is_superuser(user: schemas.User) -> bool:
     return user.is_superuser
