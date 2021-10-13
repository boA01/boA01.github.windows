'''
数据库配置相关
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@118.190.201.50:3306/test"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, encoding="utf-8", echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()