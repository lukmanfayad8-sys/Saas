#MAIN.PY
from fastapi import FastAPI
from routes import users, tasks, teams, dashboard, settings

app = FastAPI(title="Flowdesk API")

app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(tasks.router, prefix="/api/tasks", tags=["Tasks"])
app.include_router(teams.router, prefix="/api/teams", tags=["Teams"])
app.include_router(dashboard.router, prefix="/api/dashboard", tags=["Dashboard"])
app.include_router(settings.router, prefix="/api/settings", tags=["Settings"])

@app.get("/")
def root():
    return {"message": "Flowdesk API Running"}

