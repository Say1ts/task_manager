from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Замените эти значения на вашу конфигурацию
username = "postgres"
password = "admin"
host = "localhost"
port = "5432"
database = "postgres"

DATABASE_URL = f"postgresql://{username}:{password}@{host}:{port}/{database}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base: DeclarativeMeta = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
