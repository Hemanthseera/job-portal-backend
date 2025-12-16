from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# database & models
from .database import engine
from .models import Base

# routes
from .routes import users

from .dependencies import get_current_user
from fastapi import Depends
from .routes import jobs
from .routes import applications




app = FastAPI()

# CORS (React ↔ FastAPI)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# create database tables
Base.metadata.create_all(bind=engine)

# include routes
app.include_router(users.router)
app.include_router(jobs.router)
app.include_router(applications.router)



@app.get("/")
def root():
    return {"message": "FastAPI backend running 🚀"}

@app.get("/protected")
def protected_route(user=Depends(get_current_user)):
    return {
        "message": "You are authenticated",
        "user": user
    }

