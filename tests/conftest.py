from utils import setup_database, clean_data
import pytest
from battlemap.models.players import PlayerModel
from sqlalchemy import delete


@pytest.fixture(scope='session')
def database():
    """
    Sets up a database before running a test.
    """
    # Context manager lets you use yield statement which lets you run stuff before and after a function call using the "with" clause.
    return setup_database()


@pytest.fixture()
def cleanup(database):
    """
    Removes data from the database after every test.
    """
    try:
        # Let the test run.
        yield database
    finally:
        clean_data(database)