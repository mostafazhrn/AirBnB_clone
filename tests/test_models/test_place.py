#!/usr/bin/python3
"""This module shall contain the unittests for place.py"""
import unittest
import models
import os
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace(unittest.TestCase):
    """This is the TestPlace class unitest instacne"""

    def test_without_args(self):
        self.assertEqual(Place, type(Place()))

    def test_with_kwargs(self):
        self.assertEqual(Place, type(Place(**{})))

    def test_with_None(self):
        self.assertEqual(Place, type(Place(None)))

    def test_with_id(self):
        self.assertEqual(Place, type(Place(id="")))

    def test_with_created_at(self):
        self.assertEqual(Place, type(Place(created_at="")))

    def test_with_updated_at(self):
        self.assertEqual(Place, type(Place(updated_at="")))

    def test_public_datetime_created_at(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_different_places_created_at(self):
        pl1 = Place()
        sleep(0.1)
        pl2 = Place()
        self.assertNotEqual(pl1.created_at, pl2.created_at)

    def test_unused_args(self):
        pl = Place(None)
        self.assertNotIn(None, pl.__dict__.values())


if __name__ == "__main__":
    unittest.main()
