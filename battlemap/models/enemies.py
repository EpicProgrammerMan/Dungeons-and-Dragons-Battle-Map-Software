from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from battlemap.models.base import Base

# Creates a simple SQLalchemy model
# All users will have a PlayerModel, which contains various information about them
class EnemyModel(Base):
    __tablename__ = 'enemies'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False) # Enemy display name
    type = Column(String, nullable=False) # The type of enemy it is (for example: zombie, griffon, dragon)
    # gridX = Column(int) # The x position of the enemy on the grid
    # gridY = Column(int) # The y position of the enemy on the grid
    # hitpoints = Column(int, nullable=False)
    created = Column(DateTime, default=datetime.utcnow)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    # If you print an enemy, this is what is outputted
    def __repr__(self):
        return (
            f'EnemyModel(id={self.id}'
            f'name={self.name}'
            f'type={self.type}'
            f'created={self.created})'
        )