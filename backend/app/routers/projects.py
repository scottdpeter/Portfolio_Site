from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.project import ProjectCreate, ProjectRead
from app import crud

router = APIRouter()


@router.get("/", response_model=list[ProjectRead])
async def list_projects(db: AsyncSession = Depends(get_db)):
    return await crud.projects.get_all(db)


@router.post("/", response_model=ProjectRead)
async def create_project(project: ProjectCreate, db: AsyncSession = Depends(get_db)):
    return await crud.projects.create(db, project)
