import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import SessionLocal, get_db
from app.main import app
import asyncio

# Set the event loop policy for compatibility with asyncpg
asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())

@pytest.fixture(scope="session")
def event_loop():
    """
    Override the default pytest-asyncio event loop fixture to use the session-scoped loop.
    """
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
async def db_session():
    """
    Fixture to provide a database session for tests.
    """
    async with SessionLocal() as session:
        yield session

@pytest.fixture
def override_get_db(db_session):
    """
    Fixture to override the `get_db` dependency with the test database session.
    """
    async def _get_db_override():
        async for session in db_session:  # Ensure the generator is consumed properly
            yield session
    app.dependency_overrides[get_db] = _get_db_override
    yield
    app.dependency_overrides.clear()