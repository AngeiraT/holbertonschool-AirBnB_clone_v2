#!/usr/bin/python3
""" SQL db """
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.schema import MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import Base

username = getenv('HBNB_MYSQL_USER')
password = getenv('HBNB_MYSQL_PWD')
db = getenv('HBNB_MYSQL_DB')
host = getenv('HBNB_MYSQL_HOST')
v_env = getenv('HBNB_ENV')

URI = f"mysql+mysqldb://{username}:{password}@{host}/{db}"


class DBStorage:
    """db"""

    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(URI, pool_pre_ping=True)
        
        if env == "test":
            metadata = MetaData(self.__engine)
            metadata.reflect()
            metadata.drop_all()

    def all(self, cls=None):
        """ Show all class objects in DB storage or specified class """
        classDict = {"City": City, "State": State,
                     "User": User, "Place": Place,
                     "Review": Review, "Amenity": Amenity}
        objects = {}
        if cls is None:
            for className in classDict:
                data = self.__session.query(classDict[className]).all()
                for obj in data:
                    objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

        else:
            if isinstance(cls, str):
                cls = classDict[cls]
            data = self.__session.query(cls).all()
            for obj in data:
                objects[f"{obj.id}"] = obj
        return objects

    def new(self, obj):
        """Add the object to the current DB session"""
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete object from current DB session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Reload all tables and session from the engine """
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        Session = scoped_session(self.__session)
        self.__session = Session()

    def close(self):
        """ Close Session """
        self.__session.close()

    