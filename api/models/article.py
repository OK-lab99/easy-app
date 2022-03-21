from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from db import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User

#UserモデルとDBテーブルを紐付ける
class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    title =  Column(String, index=True)
    content = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="articles")