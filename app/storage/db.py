from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.common.settings import get_settings

class Base(DeclarativeBase):
    pass

settings = get_settings()
engine = create_engine(settings.DB_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
