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
from sqlalchemy.schema import MetaData


classDict = {"City": City, "State": State,
             "User": User, "Place": Place,
             "Review": Review, "Amenity": Amenity}

class DBStorage:
    """db"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                            .format(user, pwd, host, db),pool_pre_ping=True)
        
        if getenv('HBNB_ENV') == "test":
            metadata = MetaData(self.__engine)
            metadata.reflect()
            metadata.drop_all()

    def all(self, cls=None):
        """ Show all class objects in DB storage or specified class """
        dictionary = {}

        if cls is None:
            result = self.__session.query(
                     Amenity, City, State, Place, Review, User).all()
        else:
            result = self.__session.query(cls).all()

        for obj in result:
            dictionary[obj.__class__.__name__ + '.' + obj.id] = obj

        return dictionary

    def new(self, obj):
        """Add the object to the current DB session"""
        self.__session.add(obj)
        self.save()

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete object from current DB session """
        if obj:
            self.__session.delete(obj)
        self.save()

    def reload(self):
        """ Reload all tables and session from the engine """
        Base.metadata.create_all(self.__engine)
        
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ Close Session """
        self.__session.remove()

    