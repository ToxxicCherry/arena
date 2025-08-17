from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    tg_id = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    characters = relationship("Character", back_populates="owner")