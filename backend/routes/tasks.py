#TASKS.PY

from fastapi import APIRouter
from models import Task
from database import tasks_collection
from bson import ObjectId

router = APIRouter()

@router.post("/stats")
def create_task(task: Task):
    tasks_collection.insert_one(task.dict())
    return {"message": "Task added"}

@router.get("/stats")
def get_tasks():
    tasks = []
    for task in tasks_collection.find():
        task["_id"] = str(task["_id"])
        tasks.append(task)
    return tasks

@router.delete("/{task_id}")
def delete_task(task_id: str):
    tasks_collection.delete_one({"_id": ObjectId(task_id)})
    return {"message": "Task deleted"}
