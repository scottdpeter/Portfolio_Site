from sqlalchemy.ext.asyncio import AsyncSession
from app.models.contact import ContactMessage
from app.schemas.contact import ContactMessageCreate


async def create(db: AsyncSession, data: ContactMessageCreate) -> ContactMessage:
    msg = ContactMessage(**data.model_dump())
    db.add(msg)
    await db.commit()
    await db.refresh(msg)
    return msg
