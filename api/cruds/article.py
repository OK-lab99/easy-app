from sqlalchemy.orm import Session
import models, schemas
from fastapi.encoders import jsonable_encoder
from typing import List


#idからarticle取得
def get_article(db: Session, id: int) -> models.Article:
     return db.query(models.Article).filter(models.Article.id == id).first()

#article全取得
def get_articles(db: Session) -> List[models.Article]:
     articles = db.query(models.Article).all()
     return articles

#ArticleCreateの型を基にdbにポストする
def create_article(db: Session, article: schemas.ArticleCreate) -> models.Article:
     db_article = models.Article(title=article.title, content=article.content)
     db.add(db_article)
     db.commit()
     db.refresh(db_article)
     return db_article

#Update
def update_article(db: Session, article: schemas.ArticleUpdate, id: int) -> models.Article:
     #user = jsonable_encoder(user)
     db_obj = db.query(models.Article).get(id)

     if db_obj:
          db_obj.title = article.title
          db_obj.content = article.content
     db.add(db_obj)
     db.commit()
     db.refresh(db_obj)
     return db_obj

#Delete
def delete_article(db: Session, id: int) ->models.Article:
     obj = db.query(models.Article).get(id)
     db.delete(obj)
     db.commit()
     return obj