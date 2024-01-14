#!/usr/bin/python3
"""This module shall contain the unittests for console.py"""
import unittest
import console
import os
import inspect
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
HBNBCommand = console.HBNBCommand


class TestConsole(unittest.TestCase):
    """This is the TestConsole class
    Attributes:
        clsdict (dict): This represent the dictionary of classes
        clsnames (list): This represent the list of class names
        clsobjs (list): This represent the list of class objects
        clsdict (dict): This represent the dictionary of classes
    """
    def setUp(self):
        """This shall set up the environment for testing"""
        self.clsdict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                        "State": State, "City": City, "Review": Review,
                        "Amenity": Amenity}
        self.clsnames = ["BaseModel", "User", "Place", "State", "City",
                         "Review", "Amenity"]
        self.clsobjs = [BaseModel, User, Place, State, City, Review, Amenity]
        self.console = HBNBCommand()

    def tearDown(self):
        """This shall tear down the environment for testing"""
        if os.path.isfile("file.json"):
            os.remove("file.json")
    
    def test_docstrings(self):
        """This shall test the docstrings"""
        self.assertIsNotNone(console.__doc__
                                and console.HBNBCommand.__doc__
                                and console.HBNBCommand.do_quit.__doc__
                                and console.HBNBCommand.do_EOF.__doc__
                                and console.HBNBCommand.emptyline.__doc__
                                and console.HBNBCommand.do_create.__doc__
                                and console.HBNBCommand.do_show.__doc__
                                and console.HBNBCommand.do_destroy.__doc__
                                and console.HBNBCommand.do_all.__doc__
                                and console.HBNBCommand.do_update.__doc__)
        
