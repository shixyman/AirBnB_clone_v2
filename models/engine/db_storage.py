#!usr/bin/python3
""" class for sqlAlchemy """

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from os import getenv


class DBStorage:
    """ create tables in environmental"""
    __engine = None
    __session = None
