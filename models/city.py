#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = 'cities'
    state_id = ""
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), nullable=False, Foreignkey('states.id'))
    place = relationship("Place",
                         backref='cities',
                         cascade='delete', 'delete-orphan')
