#DASHBOARD.PY
from fastapi import APIRouter
from database import tasks_collection

router = APIRouter()

@router.get("/stats")
def dashboard_stats():
    total = tasks_collection.count_documents({})
    completed = tasks_collection.count_documents({"status": "Completed"})
    pending = tasks_collection.count_documents({"status": "Pending"})
    rejected = tasks_collection.count_documents({"status": "Rejected"})

    return {
        "total": total,
        "completed": completed,
        "pending": pending,
        "rejected": rejected
    }