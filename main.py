from fastapi import FastAPI


from app.models.models import Base
from database import engine

app=FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

