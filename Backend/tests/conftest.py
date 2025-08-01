import pytest
import os
from httpx import AsyncClient
from sqlmodel import Session, SQLModel, create_engine

from app.main import app
from app.config.db_config import get_session

TEST_DATABASE_URL = os.getenv("TEST_DB_URL", "postgresql://my_test_user:test_pass@test_db:5432/my_test_db")

@pytest.fixture(name='engine')
def engine_fixture():
    engine = create_engine(TEST_DATABASE_URL)
    return engine

@pytest.fixture(name='session')
def session_fixture(engine):
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    SQLModel.metadata.drop_all(engine)

@pytest.fixture(name='client')
async def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    os.environ['APP_ENV'] = 'test'

    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

    app.dependency_overrides.clear()

