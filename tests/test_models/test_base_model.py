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

    def test_with_created_at(self):
        self.assertEqual(BaseModel, type(BaseModel(created_at="")))

    def test_with_updated_at(self):
        self.assertEqual(BaseModel, type(BaseModel(updated_at="")))


if __name__ == "__main__":
    unittest.main()
