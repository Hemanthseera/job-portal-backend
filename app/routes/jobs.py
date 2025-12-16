from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..models import Job
from ..schemas import JobCreate
from ..dependencies import get_current_user

router = APIRouter(prefix="/jobs", tags=["Jobs"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE JOB (Recruiter only)
@router.post("/")
def create_job(
    job: JobCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    if user["role"] != "recruiter":
        return {"error": "Only recruiters can post jobs"}

    new_job = Job(
        title=job.title,
        description=job.description,
        location=job.location,
        company=job.company,
        recruiter_id=user["user_id"]
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job

# GET ALL JOBS (Public)
@router.get("/")
def get_jobs(db: Session = Depends(get_db)):
    return db.query(Job).all()
