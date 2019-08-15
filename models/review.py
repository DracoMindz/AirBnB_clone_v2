#!/usr/bin/python3
"""This is the review class"""
=======
import models
from models.base_model import BaseModel
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Table
import os
>>>>>>> fcdfdb1ef1a65d1f1e7e4829215b00437e252928


class Review(BaseModel):
    """This is the class for Review
    Attributes:
        place_id: place id
        user_id: user id
        text: review description
    """
    __tablename__ = 'reviews'
=======
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        place_id = Column(String(60), nullable=False, ForeignKey('places.id'))
        user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
>>>>>>> fcdfdb1ef1a65d1f1e7e4829215b00437e252928
