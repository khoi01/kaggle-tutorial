import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base


class Database:
    _engine = None
    _session_maker = None
    Base = declarative_base()

    @classmethod
    def init(cls):
        if cls._engine is None:
            db_url = os.getenv("DATABASE_URL")
            cls._engine = create_async_engine(db_url, echo=True)
            cls._session_maker = async_sessionmaker(
                bind=cls._engine,
                class_=AsyncSession,
                expire_on_commit=False
            )

    @classmethod
    def get_engine(cls):
        if cls._engine is None:
            cls.init()
        return cls._engine

    @classmethod
    def get_session(cls):
        if cls._session_maker is None:
            cls.init()
        return cls._session_maker()

    @classmethod
    async def get_db(cls):
        async with cls.get_session() as session:
            yield session
