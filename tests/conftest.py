from utils import setup_database
import pytest


@pytest.fixture(scope='session')
def database():
    """
    Sets up a database before running a test.
    """
    setup_database()