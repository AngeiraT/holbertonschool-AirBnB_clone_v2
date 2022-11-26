#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey
from os import getenv

class Amenity(BaseModel, Base):
    """
    Amenity inherits from BaseModel and Base (respect the order)
    """
    
    if getenv("HBNB_TYPE_STORAGE") == "db":
        class Amenity(BaseModel, Base):
            __tablename__ = 'amenities'
            name = Column(String(128), nullable=False)
            places_amenities = relationship(
            "Place",
            secondary="place_amenity")
    else:
        class Amenity(BaseModel);
        """Create class Amenity"""
        name = ""
