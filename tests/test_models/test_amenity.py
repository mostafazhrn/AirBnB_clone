#!/usr/bin/python3
"""This module shall contain the unittests for amenity.py"""
import unittest
import models
import os
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """This is the TestAmenity class
    Attributes:
        clsdict (dict): This represent the dictionary of classes
        clsnames (list): This represent the list of class names
        clsobjs (list): This represent the list of class objects
        clsdict (dict): This represent the dictionary of classes
    """
    def test_new_instance(self):
        """This shall test the creation of a new instance"""
        new = Amenity()
        self.assertIsInstance(new, Amenity)
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertFalse(hasattr(new, "random_attr"))
        self.assertTrue(hasattr(new, "name"))
        self.assertEqual(new.name, "")
        self.assertEqual(new.name, "")
        self.assertEqual(new.name, "")
        self.assertEqual(new.name, "")

    def test_str(self):
        """This shall test the __str__ method"""
        new = Amenity()
        self.assertEqual(str(new), "[Amenity] ({}) {}".format(new.id,
                                                              new.__dict__))
        new.name = "School"
        self.assertEqual(str(new), "[Amenity] ({}) {}".format(new.id,
                                                              new.__dict__))


if __name__ == "__main__":
    unittest.main()
