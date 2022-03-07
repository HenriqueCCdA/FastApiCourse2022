from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


#SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5434/TodoApplicationDataBase"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


#   "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjb25kaW5nd2l0aHJvYnkiLCJpZCI6MSwiZXhwIjoxNjQ2NjY3NjA4fQ.oJ3Z1LaZ4d5Z7UGYqZou5XvOZLbmqXZw9rDUU2CFd-g"
#   "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJleGFtcGxldXNlciIsImlkIjoyLCJleHAiOjE2NDY2Njk4NzB9.uSDRAnmxOP_UaFTcSfY_c4gw2fn2XiCn1as3C-GqLKY"