#!/usr/bin/python3
"""This module shall contain the FileStorage class"""

import json
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from os import path
from hashlib import md5

clsses = {"BaseModel": BaseModel, "User": User, "Place": Place,
            "State": State, "City": City, "Review": Review, "Amenity": Amenity}


class FileStorage:
    """This is the FileStorage class
    Attributes:
        __file_path (str): This represent the file path
        __objects (dict): This represent the objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """This shall return the dictionary"""
        if cls is None:
            return self.__objects
        else:
            new_dict = {}
            for k, v in self.__objects.items():
                if cls == v.__class__.__name__:
                    new_dict[k] = v
            return new_dict
        
    def new(self, obj):
        """This shall set the obj with the key"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """This shall save the file"""
        new_dict = {}
        for k, v in self.__objects.items():
            new_dict[k] = v.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """This shall reload the file"""
        if path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                new_dict = json.load(f)
                for k, v in new_dict.items():
                    self.__objects[k] = clsses[v["__class__"]](**v)

    def delete(self, obj=None):
        """This shall delete the obj"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            del self.__objects[key]
            self.save()

    def close(self):
        """This shall call reload"""
        self.reload()
