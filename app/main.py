from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from .routes import users, jobs, applications
from .dependencies import get_current_user

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
