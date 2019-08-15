#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base, Column, String
from sqlalchemy.orm import relationship
import os


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __tablename__ = 'User'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    place = relationship("Place",
                         back_populates='user',
                         cascade='all, delete, delete-orphan')
    review = relationship("Review",
                          back_populates='user',
                          cascade='all, delete, delete-orphan')
