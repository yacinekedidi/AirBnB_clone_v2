#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from sqlalchemy import (create_engine)
from os import getenv
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from models.base_model import Base, BaseModel


class DBStorage:
    """class"""
    __engine = None
    __session = None

    def __init__(self):
        """instantiates new"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv("HBNB_MYSQL_USER"),
                                              getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"),
                                              getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query"""
        l_o = []
        if cls is None:
            for t in {State, City, Amenity, Place, Review, User}:
                l.extend(self.__session.query(t).all())
        else:
            l_o = self.__session.query(cls).all()
        return {"{}.{}".format(type(o).__name__, o.id): o for o in l_o}

    def new(self, obj):
        """new"""
        self.__session.add(obj)

    def save(self):
        """save"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reload"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """call close() method on the private session attribute (self.__session)"""
        self.__session.close()
