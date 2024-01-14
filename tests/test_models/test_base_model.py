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

    def test_without_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_with_kwargs(self):
        self.assertEqual(BaseModel, type(BaseModel(**{})))

    def test_with_None(self):
        self.assertEqual(BaseModel, type(BaseModel(None)))

    def test_with_id(self):
        self.assertEqual(BaseModel, type(BaseModel(id="")))

    def test_unused_args(self):
        self.assertEqual(BaseModel, type(BaseModel("unused")))

    def test_with_created_at(self):
        self.assertEqual(BaseModel, type(BaseModel(created_at="")))

    def test_with_updated_at(self):
        self.assertEqual(BaseModel, type(BaseModel(updated_at="")))

    def test_with_all(self):
        self.assertEqual(BaseModel, type
                         (BaseModel(id="", created_at="", updated_at="")))


class TestBaseModel_instance(unittest.TestCase):
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
        new = BaseModel()
        self.assertIsInstance(new, BaseModel)
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertFalse(hasattr(new, "random_attr"))


if __name__ == "__main__":
    unittest.main()
