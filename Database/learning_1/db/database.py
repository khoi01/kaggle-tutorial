#db/database.py

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from sqlalchemy.orm import declarative_base
import os


#load .env
load_dotenv()
#connection string
DATABASE_URL = os.getenv("DATABASE_URL")
#engine - connection to db (postgreSQL)
engine = create_async_engine(DATABASE_URL,echo=True)
#session - init session for query
SessionLocal = async_sessionmaker(bind=engine,class_=AsyncSession,expire_on_commit=False)
#Base = model/table
Base =  declarative_base()

async def get_db():
    async with SessionLocal() as session:
        yield session
