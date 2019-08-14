#!/usr/bin/python3
"""storeing db class and methods"""

import sqlachemy as db
from sqlachemy.orm import sessionmaker
from os import getenv


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

        if cls == None:
            query = self.__session.query(User, State, City, Amenity, Place, Review).all()
        else:
            query = self.__session.query(cls).all()
        return dict(query)

    def new(self, obj):
        """to add object to database"""

        try:
            newobj = obj
            self.__session.add(newobj)
        except:
            raise(UsageError("Usage: DBStorage.new(<obj>)"))

    def save(self):
        """save all changes"""
        self.__session.commit()
