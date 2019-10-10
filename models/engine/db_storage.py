#!/usr/bin/python3
"""storeing db class and methods"""

import sqlachemy as db
from sqlachemy.orm import sessionmaker
from os import getenv
import models
from models.city import City
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.base_model import BaseModel, Base


class DBStorage(BaseModel, Base):
    """contains methods for manipulation of databases"""

    __engine = None
    __session = None

    def __init__(self):
        """constructor for DB"""

        self.__engine = db.create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            getenv("HBNB_MYSQL_USER"), detenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"), getenv("HBNB_MYSQL_DB"), pool_pre_ping=True))
        Session =  sessionmaker(bind=self.__engine)
        self._session = Session()

        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """lists stored objects"""

        all_dict = {}
        list_of_classes = [State, City]
        if cls is not None:
            query = self.__session.query(cls).all()
            for obj in query:
                dict_of_obj = obj.to_dict()
                key = dict_of_obj['__class__'] + '.' + dict_of_obj['id']
                a_dict[key] = obj
        elif cls is None:
            for classes in list_of_classes:
                query = self.__session.query(classes).all()
                for obj in query:
                    dict_of_obj = obj.to_dict()
                    key = dict_of_obj['__class__'] + '.' + dict_of_obj['id']
                    a_dict[key] = obj
        return (a_dict)

    def new(self, obj):
        """to add object to database"""

        self.__session.add(obj)

    def save(self):
        """save all changes"""

        self.__session.commit()

    def delete(self, obj=None):
        """delete object from database"""

        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        task #7 Air BnB v2
        calls remove() method on private session attribute
        """
        self._session.remove()


