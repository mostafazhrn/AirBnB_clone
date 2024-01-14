#!/usr/bin/python3
"""This module shall contain the unittests for base_model.py"""

import unittest
import models
import os
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """This is the test instance for BaseModel"""
    def setUp(self):
        """This shall set up the environment for testing"""
        self.base = BaseModel()

    def tearDown(self):
        """This shall tear down the environment for testing"""
        if os.path.isfile("file.json"):
            os.remove("file.json")

    def test_new_instance(self):
        """This shall test the creation of a new instance"""
        new = self.base
        self.assertIsInstance(new, BaseModel)
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertFalse(hasattr(new, "random_attr"))

    def test_str(self):
        """This shall test the __str__ method"""
        new = self.base
        self.assertEqual(str(new), "[BaseModel] ({}) {}".
                         format(new.id, new.__dict__))
        new.name = "School"
        self.assertEqual(str(new), "[BaseModel] ({}) {}".
                         format(new.id, new.__dict__))

    def test_save(self):
        """This shall test the save method"""
        new = self.base
        old = new.updated_at
        sleep(0.1)
        new.save()
        self.assertNotEqual(old, new.updated_at)


if __name__ == "__main__":
    unittest.main()
