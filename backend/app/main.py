from fastapi import FastAPI
from app.routers import projects

app = FastAPI(title="Portfolio API")

app.include_router(projects.router, prefix="/api/projects", tags=["projects"])


@app.get("/")
def root():
    return {"status": "ok"}
