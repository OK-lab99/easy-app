from fastapi import APIRouter
from fastapi import Response, Request, Depends
from fastapi.encoders import jsonable_encoder
import schemas
from fastapi import Depends, FastAPI, HTTPException, status
from cruds import user as crud
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from db import SessionLocal, engine
from dependency import get_db, get_current_user
from typing import Any, Dict, Optional, Union, List
import models

router = APIRouter()




@router.get("/user/{id}", response_model=schemas.User)
def read_user(id: int, db: Session = Depends(get_db)) -> Any:

    return crud.get_user(db, id=id)

#create
@router.post("/user", response_model=schemas.User)
def create_user(
    user: schemas.UserCreate, 
    db: Session = Depends(get_db),
) -> Any:

    db_user = crud.get_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    
    db_user = crud.create_user(db, user=user)
    return db_user

#ユーザー設定取得
@router.get("/me", response_model=schemas.User)
def read_user_me(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
) -> Any:
    """ 
    Get current user.
    """
    return current_user