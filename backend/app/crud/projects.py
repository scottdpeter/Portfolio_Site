from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.project import Project
from app.schemas.project import ProjectCreate


async def get_all(db: AsyncSession) -> list[Project]:
    result = await db.execute(select(Project))
    return result.scalars().all()


async def create(db: AsyncSession, data: ProjectCreate) -> Project:
    project = Project(**data.model_dump())
    db.add(project)
    await db.commit()
    await db.refresh(project)
    return project
