# DATABASE.PY
from pathlib import Path
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import logging

logger = logging.getLogger(__name__)

# Load .env located at backend/env/.env (explicit path so load works regardless of CWD)
env_path = Path(__file__).parent / "env" / ".env"
load_dotenv(dotenv_path=env_path)

# Prefer `MONGODB_URL`; fallback to legacy `MONGO_URL` for compatibility
MONGODB_URL = os.getenv("MONGODB_URL") or os.getenv("MONGO_URL")
if not MONGODB_URL:
	raise RuntimeError(
		"MONGODB_URL not set. Set it in environment or in backend/env/.env as MONGODB_URL"
	)

# Allow configuring the database name via env, default to 'flowdesk'
DB_NAME = os.getenv("MONGODB_DB") or os.getenv("DB_NAME") or "flowdesk"

# Create client with a short server selection timeout to fail fast on bad config
try:
	client = MongoClient(MONGODB_URL, serverSelectionTimeoutMS=5000)
	# Force a call to the server to validate connection/config early
	client.server_info()
except Exception as exc:
	logger.exception("Failed to connect to MongoDB at %s", MONGODB_URL)
	raise RuntimeError("Unable to connect to MongoDB. Check MONGODB_URL and network connectivity") from exc

# Database and collections
db = client[DB_NAME]

# Export commonly used collections for convenience
users_collection = db["users"]
tasks_collection = db["tasks"]
teams_collection = db["teams"]


def get_db():
	"""Return the database instance. Useful for dependency injection or tests."""
	return db


def get_client():
	"""Return the underlying MongoClient."""
	return client