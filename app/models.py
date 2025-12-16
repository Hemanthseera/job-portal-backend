from sqlalchemy import Column, Integer, String, Text, ForeignKey, UniqueConstraint
from .database import Base

# ---------------- USER ----------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)


# ---------------- JOB ----------------
class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    location = Column(String, nullable=False)
    company = Column(String, nullable=False)

    recruiter_id = Column(Integer, ForeignKey("users.id"))


# ---------------- APPLICATION ----------------
class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    job_id = Column(Integer, ForeignKey("jobs.id"))

    __table_args__ = (
        UniqueConstraint("user_id", "job_id", name="unique_user_job"),
    )
