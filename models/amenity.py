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
    __tablename__ = 'amenities'
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        places_amenities = relationship(
            "Place",secondary="place_amenity")
    else:
        class Amenity(BaseModel):
            """Create class Amenity"""
            name = ""
            state_id = ""
