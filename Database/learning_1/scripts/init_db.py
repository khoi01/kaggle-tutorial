import asyncio
from db.database import engine,Base
from models import *  # imports User and any future models

async def init_db():
    async with engine.begin() as conn:
        print("creating tables..")
        await conn.run_sync(Base.metadata.create_all)
        print("table is created..")
        
if __name__ == "__main__":
    asyncio.run(init_db())