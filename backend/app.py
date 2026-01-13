#MAIN.PY
from fastapi import FastAPI
from routes import users, tasks, teams, dashboard, settings
from database import get_client

app = FastAPI(title="Flowdesk API")

origins =[
    "http://localhost:5500",
    "http://127.0.0.1:5500"
]

app.add_middleware(CORSMiddleware,allow_origins=origins,allow_credentials=True,allow_methods=["*"],allow_headers=["*"],)

app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(tasks.router, prefix="/api/tasks", tags=["Tasks"])
app.include_router(teams.router, prefix="/api/teams", tags=["Teams"])
app.include_router(dashboard.router, prefix="/api/dashboard", tags=["Dashboard"])
app.include_router(settings.router, prefix="/api/settings", tags=["Settings"])


@app.get("/")
def root():
    return {"message": "Flowdesk API Running"}


@app.get("/health")
def health_check():
    """Health check endpoint that also validates MongoDB connectivity."""
    try:
        client = get_client()
        # ping the server
        client.admin.command('ping')
        return {"status": "ok", "db": "connected"}
    except Exception as exc:
        return {"status": "error", "db": "unreachable", "detail": str(exc)}

