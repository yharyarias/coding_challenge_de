from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext import declarative_base

SQLALCHEMY_DATA = "sqlite:///./data.db"

engine = create_engine(
    SQLALCHEMY_DATA, connect_args={"check_same_thread":False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

