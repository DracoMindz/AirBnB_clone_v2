#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base
from models.place import place_amenity
import os
from sqlalchemy import Column, String, Integer, Table
from sqlalchemy.orm import relationship, backref


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = 'amenities'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Places",
                                       secondary='place_amenity',
                                       back_populates='amenities')
    else:
        name = ""
