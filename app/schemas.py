from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    username: str | None = None
    tg_id: str


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
    