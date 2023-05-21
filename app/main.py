from fastapi import FastAPI
from . import models
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from .config import settings
from .routers import posts, user, auth, vote
from pydantic import BaseSettings

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["https://www.google.com",
           "https://www.youtube.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello World!"}