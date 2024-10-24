from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from config import settings

base_url = f"postgresql+asyncpg://{settings.db_user}:{settings.db_pass}@{settings.db_host}:{settings.db_port}/{settings.db_name}"

engine = create_async_engine(
    url=base_url,
)

Session = async_sessionmaker(
    bind=engine
)


class Base(DeclarativeBase, AsyncAttrs):
    __abstart__ = True
