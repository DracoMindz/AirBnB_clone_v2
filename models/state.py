#!/usr/bin/python3
"""This is the state class"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class State(BaseModel):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(string(128), nullable=False)
        cities = relationship("City",
                              cascade="all, delete-orphan",
                              back_populates="state")

    else:
        name = ""

        @property
        def cities(self):
            """getter for cities"""
            cities_instances = []
            cities_dict = models.storage.all(City)
            for key, value in cities_dict.items():
                if self.id == value.state_id:
                    cities_instances.append(value)
            return cities_instances
