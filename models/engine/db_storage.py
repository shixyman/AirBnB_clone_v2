#!usr/bin/python3
""" class for sqlAlchemy """

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from os import getenv
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """ create tables in environmental"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv("HBNB_MYSQL_USER"), getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"), getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def new(self, obj):
        """add a new element in the table
        """
        self.__session.add(obj)

    def save(self):
        """save changes
        """
        self.__session.commit()
    def delete(self, obj):
        """delete an element in the table
        """
        self.__session.delete(obj)

    def all(self, cls):
        """return all elements of a table
        """
        return self.__session.query(cls).all()

    def reload(self):
        """reload the tables
        """
        Base.metadata.create_all(self.__engine)

    def rollback(self):
        """rollback the changes
        """
        self.__session.rollback()

    def close(self):
        """close the session
        """
        self.__session.close()
