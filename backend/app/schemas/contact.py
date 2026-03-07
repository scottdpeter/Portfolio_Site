from pydantic import BaseModel, EmailStr
from datetime import datetime


class ContactMessageCreate(BaseModel):
    name: str
    email: EmailStr
    message: str


class ContactMessageRead(ContactMessageCreate):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}
