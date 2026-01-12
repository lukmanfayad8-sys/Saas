# Settings

from fastapi import APIRouter, Depends, HTTPException
from database import users_collection
from bson import ObjectId

from auth import get_current_user

router = APIRouter()


@router.put("/{user_id}")
def update_user(user_id: str, name: str, email: str, current_user: dict = Depends(get_current_user)):
    result = users_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": {"name": name, "email": email}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated"}


@router.delete("/{user_id}")
def delete_user(user_id: str, current_user: dict = Depends(get_current_user)):
    result = users_collection.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "Account deleted"}