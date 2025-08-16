from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.database import get_db

app = FastAPI(title="Arena PvP Game")


@app.get("/")
async def root():
    return {"message": "Welcome to Arena PvP"}

@app.get("/ping_db")
async def ping_db(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(text("SELECT 1"))
        value = result.scalar_one()
        return {"status": "ok", "result": value}
    except Exception as e:
        return {"status": "error", "message": str(e)}