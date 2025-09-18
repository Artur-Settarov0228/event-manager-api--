from sqlalchemy import create_engine, URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app import config

# Database URL yaratish
DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username=config.DB_USER,
    password=config.DB_PASSWORD,
    host=config.DB_HOST,
    port=config.DB_PORT,
    database=config.DB_NAME,
)

# Engine va Session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Baza modeli
Base = declarative_base()

# DB session generator
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
