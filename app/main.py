from fastapi import FastAPI
from app.database import Base, engine
from app.models import User


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Event Manager API")

@app.get("/")
def home():
    return {"message": "Event Manager API is running 🚀"}
