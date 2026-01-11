# MODELS
 from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: Optional[str] = "user"

class Task(BaseModel):
    title: str
    description: str
    priority: str
    assigned_to: str
    status: Optional[str] = "Pending"

class Team(BaseModel):
    name: str
    email: EmailStr
    phone: str
