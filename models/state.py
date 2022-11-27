#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from os import getenv




class State(BaseModel, Base):
        """ State class """
        __tablename__ = "states"
        if getenv("HBNB_TYPE_STORAGE") == "db":
            name = Column(String(128), nullable=False)
            cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
        else:
            name = ""
            
            @property
            def cities(self):
                """ Returns a list of all cities in state """
                return [city for city in models.storage.all(City).values() if
                    self.id == city.state_id]

