from battlemap.models.database import init_engine
import subprocess

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