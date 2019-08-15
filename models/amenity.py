#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel
from models.place import place_amenity
import os
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship



class Amenity(BaseModel):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place',
                                   secondary=place_amenity,
                                   back_populates='amenities')
