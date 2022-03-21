from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#スキーマ://ユーザー:パスワード@docker内のservice(host)/データベース名

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@db/postgres"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base() #modelを作成するため