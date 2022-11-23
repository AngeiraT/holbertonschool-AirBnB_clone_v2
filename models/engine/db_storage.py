#!/usr/bin/python3
""" SQL db """
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import Base

class DBStorage:
    """db"""

    __engine = None
    __session = None

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine("mysql+pymysql://{}:{}@{}/{}"
                            .format(user, pwd, host, db),pool_pre_ping=True)
        
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Show all class objects in DB storage or specified class """
        if cls:
            objects = self.__session.query(cls).all()
        else:
            classes = [State, City, User, Place, Review, Amenity]
            objects = []
            for c in classes:
                objects += self.__session.query(c)
        return {"{}.{}".format(type(obj).__name__, obj.id): obj for obj in
                objects}
