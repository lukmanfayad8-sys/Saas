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
        from datetime import datetime, timedelta
        import os
        from typing import Optional

        from fastapi import APIRouter, Depends, HTTPException, status
        from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
        from jose import JWTError, jwt
        from passlib.context import CryptContext

        from database import users_collection

        router = APIRouter()

        # Password hashing
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

        # JWT config (set `SECRET_KEY` in env for production)
        SECRET_KEY = os.getenv("SECRET_KEY", "change-me-super-secret")
        ALGORITHM = "HS256"
        ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

        oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/users/token")


        def verify_password(plain_password: str, hashed_password: str) -> bool:
            return pwd_context.verify(plain_password, hashed_password)


        def get_password_hash(password: str) -> str:
            return pwd_context.hash(password)


        def authenticate_user(email: str, password: str):
            user = users_collection.find_one({"email": email})
            if not user:
                return None
            if not verify_password(password, user.get("password", "")):
                return None
            return user


        def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
            to_encode = data.copy()
            if expires_delta:
                expire = datetime.utcnow() + expires_delta
            else:
                expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            to_encode.update({"exp": expire})
            encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
            return encoded_jwt


        @router.post("/token")
        def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
            user = authenticate_user(form_data.username, form_data.password)
            if not user:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Incorrect username or password",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = create_access_token(
                data={"sub": user["email"]}, expires_delta=access_token_expires
            )
            return {"access_token": access_token, "token_type": "bearer"}


        def get_current_user(token: str = Depends(oauth2_scheme)):
            credentials_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
            try:
                payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
                email: str = payload.get("sub")
                if email is None:
                    raise credentials_exception
            except JWTError:
                raise credentials_exception
            user = users_collection.find_one({"email": email})
            if user is None:
                raise credentials_exception
            return user
