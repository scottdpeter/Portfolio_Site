from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.contact import ContactMessageCreate, ContactMessageRead
from app.crud import contact

router = APIRouter()


@router.post("/", response_model=ContactMessageRead, status_code=201)
async def submit_contact(data: ContactMessageCreate, db: AsyncSession = Depends(get_db)):
    return await contact.create(db, data)
