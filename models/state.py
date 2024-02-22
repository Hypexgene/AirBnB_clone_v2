#!/usr/bin/python3
"""State Module for HBNB project."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class for the HBNB project."""

    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if models.storage_type == 'db':
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        @property
        def cities(self):
            """Getter attribute that returns the list of City instances
            with state_id equals to the current State.id."""
            city_list = []
            for city in models.storage.all('City').values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
