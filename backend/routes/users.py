from fastapi import APIRouter, HTTPException
from models import User
from database import users_collection
from passlib.context import CryptContext
from fastapi import Depends
from auth import get_current_user

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

@router.post("/register")
def register(user: User):
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already exists")

    user.password = hash_password(user.password)
    users_collection.insert_one(user.dict())
    return {"message": "User registered successfully"}

@router.get("/me")
def read_current_user(current_user: dict = Depends(get_current_user)):
    # return a safe representation
    return {"name": current_user.get("name"), "email": current_user.get("email"), "role": current_user.get("role")}
