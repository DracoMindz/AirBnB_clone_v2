#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object without class
        if class:
            returns list of objects of one type of class
        """

        if cls in None:
            return self.__objects
        else:
            obj_dict = {}
            if cls:
                for key, value in self.__objects.items():
                    if cls == type(value):
                        obj_dict[key] = value
            return obj_dict

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def delete(self, obj=None):
        """to delete obj from __objects if it is inside
        """
        if obj is None:
            return
        index = type(obj).__name__ + "." + obj.id
        if index is self.__objects:
            del self.__objects[index]
        FileStorage.save(self)

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def close(self):
        """
        task #7 Air BnB v2
        calls reload method for deserializing JSON file to objects
        """
        self.reload()
