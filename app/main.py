
from fastapi import FastAPI
from pydantic import BaseModel, Field
from database import Base ,engine
from models import users, events


app = FastAPI(title="Event Management API")

Base.metadata.create_all(bind=engine)

