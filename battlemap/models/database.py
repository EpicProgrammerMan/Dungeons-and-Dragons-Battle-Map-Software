# from sqlalchemy.orm import declarative_base, create_engine, scoped_session, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

def init_engine():
    """ This method will create an engine using the appropriate
    environment variables from the docker-compose file. """
    user = os.environ['POSTGRES_USER']
    password = os.environ['POSTGRES_PASSWORD']
    host = os.environ['POSTGRES_HOST']
    db = os.environ['POSTGRES_DB']
    port = os.environ['POSTGRES_PORT']
    return create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    

engine = init_engine()
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()