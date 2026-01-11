#TEAM.PY

from fastapi import APIRouter
from models import Team
from database import teams_collection
from bson import ObjectId

router = APIRouter()

@router.post("/")
def add_team(team: Team):
    teams_collection.insert_one(team.dict())
    return {"message": "Team member added"}

@router.get("/")
def get_teams():
    teams = []
    for member in teams_collection.find():
        member["_id"] = str(member["_id"])
        teams.append(member)
    return teams

@router.delete("/{team_id}")
def delete_team(team_id: str):
    teams_collection.delete_one({"_id": ObjectId(team_id)})
    return {"message": "Team member removed"}