from fastapi import FastAPI
from app.database import Base, engine
from app.models import User
from app.routers import users as users_router
from app.routers import events as events_router



app = FastAPI(title="Event Manager API")

Base.metadata.create_all(bind=engine)

app.include_router(users_router.router)
app.include_router(events_router.router)