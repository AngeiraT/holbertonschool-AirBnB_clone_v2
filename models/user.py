#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv

if getenv("HBNB_TYPE_STORAGE") == "db":
    class User(BaseModel, Base):
        """This class defines a user by various attributes"""
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship(
            "Place",
            backref="user",
            cascade="all, delete-ophan")
        reviews = relationship(
            "Review",
            backref="user",
            cascade="all, delete-orphan")
else:
    class User(BaseModel):
        '''Defined class to work with FileStorage'''
        email = ''
        password = ''
        first_name = ''
        last_name = ''
