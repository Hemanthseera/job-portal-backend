from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from ..database import SessionLocal
from ..models import Application
from ..schemas import ApplyJob
from ..dependencies import get_current_user

router = APIRouter(prefix="/applications", tags=["Applications"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/apply")
def apply_job(
    data: ApplyJob,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    if user["role"] != "jobseeker":
        return {"error": "Only jobseekers can apply"}

    application = Application(
        user_id=user["user_id"],
        job_id=data.job_id
    )

    try:
        db.add(application)
        db.commit()
        return {"message": "Job applied successfully"}
    except IntegrityError:
        db.rollback()
        return {"error": "You already applied for this job"}
