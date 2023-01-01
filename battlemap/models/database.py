# from sqlalchemy.orm import declarative_base, create_engine, scoped_session, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

def init_engine(db_name = None, **kwargs):
    """ This method will create an engine using the appropriate
    environment variables from the docker-compose file. """
    user = os.environ['POSTGRES_USER']
    password = os.environ['POSTGRES_PASSWORD']
    host = os.environ['POSTGRES_HOST']
    # Pass in a database name if you want to connect to a different database
    db = db_name or os.environ['POSTGRES_DB']
    port = os.environ['POSTGRES_PORT']
    return create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}', **kwargs)

engine = init_engine()
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()