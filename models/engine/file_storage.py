#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if type(cls) is str:
            cls = eval(cls)
        if cls is not None:
            return {k: v for k, v in self.__objects.items()
                    if cls.__name__ in k}
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects[obj.to_dict()['__class__'] + '.' + obj.id] = obj

    def save(self):
        """Saves storage dictionary to file"""
        tmp = {o: self.__objects[o].to_dict() for o in self.__objects.keys()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(tmp, f)

    def reload(self):
        """Loads storage dictionary from file"""

        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for o in temp.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """deletes instances"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """Call the reload method."""
        self.reload()
