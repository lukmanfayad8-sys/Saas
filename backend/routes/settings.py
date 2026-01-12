#Settings

from fastapi import APIRouter
from database import users_collection
from bson import ObjectId

router = APIRouter()

@router.put("/{user_id}")
def update_user(user_id: str, name: str, email: str):
    users_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": {"name": name, "email": email}}
    )
    return {"message": "User updated"}

@router.delete("/{user_id}")
def delete_user(user_id: str):
    users_collection.delete_one({"_id": ObjectId(user_id)})
    return {"message": "Account deleted"}