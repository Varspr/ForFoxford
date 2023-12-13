from contextlib import asynccontextmanager

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from database.config import service_database_settings

engine = create_async_engine(service_database_settings.postgresql_url, echo=True)
async_session = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
meta = MetaData()


@asynccontextmanager
async def get_session():
    async with async_session() as session:
        await session.begin()
        await session.close()

