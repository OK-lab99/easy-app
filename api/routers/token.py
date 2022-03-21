from datetime import timedelta
from typing import Any
from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import models, schemas
from cruds import user as crud
from dependency import get_db, get_current_user
from utils.auth_utils import create_access_token, get_password_hash, verify_password

ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter()

#usernameとpasswordを送信しTokenを発行

@router.post('/token')
def get_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.name == form_data.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Invalid credentials'
        )
    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Incorrect password'
        )
    access_token = create_access_token(data={'sub': user.name})
    return {
        'access_token': access_token,
        'token_type': 'bearer',
        'user_id': user.id,
        'username': user.name
    }