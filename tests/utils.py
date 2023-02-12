from battlemap.models.database import init_engine
import subprocess
from sqlalchemy.orm import scoped_session, sessionmaker
from battlemap.models.players import PlayerModel
from sqlalchemy import delete

POSTGRES = 'postgres'


def setup_database():
    """
    Recreate a database template for testing.
    """
    # Recreate the testing database.
    with init_engine(POSTGRES, isolation_level='AUTOCOMMIT').connect() as connection:
        connection.execute(f'DROP DATABASE IF EXISTS battlemap')
        connection.execute(f'CREATE DATABASE battlemap WITH owner battlemap')

    # Run alembic to upgrade the database.
    result = subprocess.run(['alembic', 'upgrade', 'heads'])
    output = result.stdout or result.stderr
    if output:
        print(output.strip())
    
    # Return an active session to the database.
    engine = init_engine()
    return scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

def clean_data(db_session):
    stmt = delete(PlayerModel)
    db_session.execute(stmt)
    db_session.commit()