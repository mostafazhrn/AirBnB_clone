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

    def all(self):
        """This shall return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """This shall set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """ This shall serialize __objects to the JSON file __file_path"""
        dictobj = FileStorage.__objects
        objdict = {obj: dictobj[obj].to_dict() for obj in dictobj.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """This shall deserialize the JSON file __file_path
        to __objects, if it exists"""
        if path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
