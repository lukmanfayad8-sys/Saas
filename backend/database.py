#DATABASE.PY
from pathlib import Path
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load .env located at backend/env/.env (explicit path so load works regardless of CWD)
env_path = Path(__file__).parent / "env" / ".env"
load_dotenv(dotenv_path=env_path)

# Prefer `MONGODB_URL`; fallback to legacy `MONGO_URL` for compatibility
MONGO_URL = os.getenv("MONGODB_URL") or os.getenv("MONGO_URL")
if not MONGO_URL:
	raise RuntimeError(
		"MONGODB_URL not set. Set it in environment or in backend/env/.env as MONGODB_URL"
	)

# Create client with a short server selection timeout to fail fast on bad config
client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=5000)
db = client["flowdesk"]

users_collection = db["users"]
tasks_collection = db["tasks"]
teams_collection = db["teams"]