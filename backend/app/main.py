from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import projects, contact

app = FastAPI(title="Portfolio API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"],  # Live Server default ports
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(projects.router, prefix="/api/projects", tags=["projects"])
app.include_router(contact.router, prefix="/api/contact", tags=["contact"])


@app.get("/")
def root():
    return {"status": "ok"}
