#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel
from models.amenity import Amenity
import os
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship, backref



class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place-amenities = relationship("Many-To-Many",
