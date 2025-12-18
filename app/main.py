from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from .database import engine
from .models import Base
from .dependencies import get_current_user

from .routes import users, jobs, applications


app = FastAPI(title="Job Portal API")

# ✅ CORS (allow frontend + future domains)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # safe for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ CREATE TABLES SAFELY (ON STARTUP)
@app.on_event("startup")
def on_startup():
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Database tables created")
    except Exception as e:
        print("❌ Database connection failed:", e)


# ✅ ROUTES
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(jobs.router, prefix="/jobs", tags=["Jobs"])
app.include_router(applications.router, prefix="/applications", tags=["Applications"])


# ✅ HEALTH CHECK
@app.get("/")
def root():
    return {"message": "Job Portal Backend running on Render 🚀"}


# ✅ AUTH TEST
@app.get("/protected")
def protected_route(user=Depends(get_current_user)):
    return {
        "message": "You are authenticated",
        "user": user
    }
