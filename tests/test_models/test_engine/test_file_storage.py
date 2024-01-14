#!/usr/bin/python3
"""This module shall contain the unittests for file_storage.py"""
import unittest
import models
import os
import json
from datetime import datetime
from time import sleep
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity


class TestFileStorage(unittest.TestCase):
    """THis is the test instance for FileStorage"""

    def test_without_args(self):
        self.assertEqual(FileStorage, type(FileStorage()))

    def test_with_kwargs(self):
        self.assertEqual(FileStorage, type(FileStorage(**{})))

    def test_with_None(self):
        self.assertEqual(FileStorage, type(FileStorage(None)))

    def test_with_id(self):
        self.assertEqual(FileStorage, type(FileStorage(id="")))

    def test_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage("unused")

    def test_with_all(self):
        self.assertEqual(FileStorage, type
                         (FileStorage(id="", created_at="", updated_at="")))


class TestFileStorage_instance(unittest.TestCase):
    """This is the test instance for FileStorage"""

    def setUp(self):
        """This shall set up the environment for testing"""
        self.storage = FileStorage()

    def tearDown(self):
        """This shall tear down the environment for testing"""
        if os.path.isfile("file.json"):
            os.remove("file.json")

    def test_new_instance(self):
        """This shall test the creation of a new instance"""
        new = FileStorage()
        self.assertIsInstance(new, FileStorage)
        self.assertTrue(hasattr(new, "_FileStorage__file_path"))
        self.assertTrue(hasattr(new, "_FileStorage__objects"))
        self.assertEqual(new._FileStorage__file_path, "file.json")
        self.assertIsInstance(new._FileStorage__objects, dict)

    def test_all(self):
        """This shall test the all method"""
        self.assertIsInstance(self.storage.all(), dict)
        self.assertEqual(self.storage.all(), {})
        self.storage.new(BaseModel())
        self.assertIsInstance(self.storage.all(), dict)
        self.assertNotEqual(self.storage.all(), {})
        self.storage.new(User())
        self.assertIsInstance(self.storage.all(), dict)
        self.assertNotEqual(self.storage.all(), {})
        self.storage.new(Place())
        self.assertIsInstance(self.storage.all(), dict)
        self.assertNotEqual(self.storage.all(), {})
        self.storage.new(State())
        self.assertIsInstance(self.storage.all(), dict)
        self.assertNotEqual(self.storage.all(), {})
        self.storage.new(City())
        self.assertIsInstance(self.storage.all(), dict)
        self.assertNotEqual(self.storage.all(), {})
        self.storage.new(Review())
        self.assertIsInstance(self.storage.all(), dict)
        self.assertNotEqual(self.storage.all(), {})
        self.storage.new(Amenity())
        self.assertIsInstance(self.storage.all(), dict)
        self.assertNotEqual(self.storage.all(), {})


if __name__ == "__main__":
    unittest.main()
