from sqlalchemy import (
    create_engine,
    URL,

)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config 

DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username=config.DB_USER,
    password=config.DB_PASSWORD,
    host=config.DB_HOST,
    port=config.DB_PORT,
    database=config.DB_NAME,
)
engine = create_engine(DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
        