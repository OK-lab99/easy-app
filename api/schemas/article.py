from pydantic import BaseModel
from datetime import date

class ArticleBase(BaseModel):
    title: str | None = None
    content: str | None = None

#post(crudで使う)
class ArticleCreate(ArticleBase):
    title: str
    content: str

#put(crudで使う)
class ArticleUpdate(ArticleBase):
    pass

#DBに格納するための型を定義(レスポンスbodyで使う)
class ArticleInDBBase(ArticleBase):
    id: int
    user_id: int | None = None
    class Config:
        orm_mode = True

#レスポンスbodyで使うスキーマ
class Article(ArticleInDBBase):
    pass

class ArticleInDB(ArticleInDBBase):
   pass