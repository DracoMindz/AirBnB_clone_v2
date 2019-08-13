#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel


class State(BaseModel):
    """This is the class for State
    Attributes:
        name: input name
    """
    name = ""
    __tablename__ = "states"
    name = Column(string(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan", back_populates="state")

    @property
    def cities(self):
    """getter for cities"""
