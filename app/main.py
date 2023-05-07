from fastapi import FastAPI
from . import models
from .database import engine
from .config import settings
from .routers import posts, user, auth, vote
from pydantic import BaseSettings

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(posts.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)