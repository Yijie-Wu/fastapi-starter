from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql+asyncpg://user:pass@localhost/db"
engine = create_async_engine(DATABASE_URL, pool_size=20, max_overflow=10)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)


app = FastAPI()


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


# @app.on_event("startup")
# async def startup():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)


async def safe_create_all():
    engine = create_async_engine(DATABASE_URL)
    async with engine.connect() as conn:
        # 检查表是否已存在
        inspector = inspect(await conn.get_schema_connection())
        existing_tables = await inspector.get_table_names()

        # 仅创建不存在的表
        tables_to_create = [
            table for table in Base.metadata.tables.keys()
            if table not in existing_tables
        ]

        if tables_to_create:
            async with engine.begin() as trans_conn:
                await trans_conn.run_sync(
                    lambda sync_conn: Base.metadata.create_all(
                        bind=sync_conn,
                        tables=[Base.metadata.tables[name] for name in tables_to_create]
                    )
                )
