from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


# Creates a simple SQLalchemy model
# All users will have a PlayerModel, which contains various information about them
class PlayerModel(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    created = Column(DateTime, default=datetime.utcnow)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return (
            f'PlayerModel(id={self.id}, first_name={self.first_name},'
            f'last_name={self.last_name}'
            f'created={self.created})'
        )