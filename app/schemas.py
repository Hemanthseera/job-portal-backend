from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str
    role: str

class UserResponse(BaseModel):
    id: int
    email: str
    role: str

    class Config:
        orm_mode = True


class LoginRequest(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class JobCreate(BaseModel):
    title: str
    description: str
    location: str
    company: str

class JobResponse(JobCreate):
    id: int
    recruiter_id: int

    class Config:
        orm_mode = True

class ApplyJob(BaseModel):
    job_id: int



