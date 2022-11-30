#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv

    
    
class Amenity(BaseModel, Base):
    """
    Amenity inherits from BaseModel and Base (respect the order)
    """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        places_amenities = relationship(
            "Place",secondary="place_amenity")
    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
