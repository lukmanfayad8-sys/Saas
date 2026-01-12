from fastapi import APIRouter, HTTPException
from models import User
from database import users_collection
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)
@router.post("/register")
 def register_user(user: User):
     if users_collection.find_one({"email": user.email}):
         raise HTTPException(status_code=400, detail="Email already exists")
     user_password = hash_password(user.password)
     
     users_collection.insert_one(user.dict())
     return
    {"message": "User registered successfully"}
    
    @router.post("/login")
    def login_user(email: str, password: str):
        user = users_collection.find_one({"email": email})
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return {"message": "Login successful"}
        
        if not pwd_context.verify(password, user["password"]):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        return {"message": "Login successful"," user": {"name": user["name"], "email": user["email"]}}