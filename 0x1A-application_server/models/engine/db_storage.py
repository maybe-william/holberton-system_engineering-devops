#!/usr/bin/python3
"""This is the db storage class for AirBnB"""
import json
import os
import models
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import (create_engine)
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __engine = None
    __session = None

    def close(self):
        """call self.__session.remove() or Session.close()"""
        DBStorage.__session.remove()

    def __init__(self):
        """init the engine and session with sqlalchemy and mysqldb"""
        user = os.environ['HBNB_MYSQL_USER']
        password = os.environ['HBNB_MYSQL_PWD']
        host = os.environ['HBNB_MYSQL_HOST']
        db = os.environ['HBNB_MYSQL_DB']

        squrl = 'mysql+mysqldb://{}:{}@{}/{}'.format(user, password, host, db)
        DBStorage.__engine = create_engine(squrl, pool_pre_ping=True)
        self.reload()

        # drop all tables if HBNB_ENV == 'test'
        if 'test' in os.environ and os.environ['HBNB_ENV'] == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of all objects
        """
        q = []
        q.extend(DBStorage.__session.query(User).all())
        q.extend(DBStorage.__session.query(State).all())
        q.extend(DBStorage.__session.query(City).all())
        q.extend(DBStorage.__session.query(Amenity).all())
        q.extend(DBStorage.__session.query(Place).all())
        q.extend(DBStorage.__session.query(Review).all())
        ret = {}
        for item in q:
            key = "{}.{}".format(type(item).__name__, item.id)
            ret[key] = item
        return ret

    def new(self, obj):
        """sets given obj in db
        Args:
            obj: given object
        """
        if obj:
            DBStorage.__session.add(obj)

    def delete(self, obj=None):
        """delete the given obj from db if not none"""
        if obj:
            DBStorage.__session.delete(obj)

    def save(self):
        """commit all changes to db
        """
        DBStorage.__session.commit()

    def reload(self):
        """create all tables in the db and create current session from engine
        """
        Base.metadata.create_all(DBStorage.__engine)
        Session = sessionmaker()
        Session.configure(bind=DBStorage.__engine)
        DBStorage.__session = scoped_session(Session)
