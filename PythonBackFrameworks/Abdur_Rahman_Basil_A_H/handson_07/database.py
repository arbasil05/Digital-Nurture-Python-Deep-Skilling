from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. The database connection string (using aiosqlite for async SQLite)
SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./courses.db"

# 2. Create the async engine (the core interface to the database)
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# 3. Create a session factory to spawn new database sessions
AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# 4. Create a Base class that our future database tables will inherit from
Base = declarative_base()

# 5. The Dependency function (Step 64)
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session