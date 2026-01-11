#DATABASE.PY
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

client = MongoClient(MONGO_URL)
db = client["flowdesk"]

users_collection = db["users"]
tasks_collection = db["tasks"]
teams_collection = db["teams"]