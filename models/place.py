#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base, Column, String
from models.base_model import Integer
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from sqlalchemy import *
import os


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'), nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), nullable=False))

class Place(BaseModel):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in i nt
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = 'places'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review',
                               back_populate='place',
                               cascade='all, delete, delete-orphan')
        amenity_ids = []

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = ""
        number_bathrooms = ""
        max_guest = ""
        price_by_night = ""
        latitude = ""
        longitude = ""
        reviews = ""
        amenity_ids = []
