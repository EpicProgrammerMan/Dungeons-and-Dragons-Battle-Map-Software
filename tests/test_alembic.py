import pytest
import sqlalchemy
@pytest.fixture
def database_engine():
    return sqlalchemy.engine