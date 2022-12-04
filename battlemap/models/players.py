from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
# The base.py file is the root of the inheritance tree
# Every model build off of base.py inherits from what is in it
from battlemap.models.database import Base

# Creates a simple SQLalchemy model
# All users will have a PlayerModel, which contains various information about them
class PlayerModel(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return (
            f'PlayerModel(id={self.id}, name={self.name},'
            f'created={self.created})'
        )