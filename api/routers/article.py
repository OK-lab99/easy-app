from fastapi import Depends, APIRouter, HTTPException

from sqlalchemy.orm import Session 
from db import SessionLocal, engine
from typing import Any, List
from dependency import get_db, get_current_user
from cruds import article as crud
import models
import schemas

router = APIRouter()

@router.get("/article/{id}", response_model = schemas.Article)
def read_article(
    id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
) -> Any:
    article = crud.get_article(db, id=id)
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

@router.get("/articles/", response_model= List[schemas.Article])
def read_articles(db: Session = Depends(get_db)) -> Any:
    articles = crud.get_articles(db)
    return articles


@router.post("/article/", response_model=schemas.Article,)
def create_article(
    article: schemas.ArticleCreate,
    db: Session = Depends(get_db)
) -> Any:
    article = crud.create_article(db, article=article)
    return article

@router.put("/article/{id}", response_model=schemas.Article)
def update_article(
    id: int,
    article: schemas.ArticleUpdate,
    db: Session = Depends(get_db),
) -> Any:
    article = crud.update_article(db, article=article, id=id)
    return article

@router.delete("/article/{id}", response_model=schemas.Article)
def delete_article(
    id: int,
    db: Session = Depends(get_db)
) -> Any:
    article = crud.delete_article(db, id=id)
    return article
