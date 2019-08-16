#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel
import os
from sqlalchemy.orm import relationship

class City(BaseModel):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = 'cities'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), Foreignkey('states.id'), nullable=False)
        state = relationship("State",
                             back_populates='cities')

    else:
        name = ""
        state_id = ""
