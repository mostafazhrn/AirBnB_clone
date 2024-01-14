#!/usr/bin/python3
"""This module shall contain the unittests for city.py"""
import unittest
import models
import os
from datetime import datetime
from time import sleep
from models.city import City


class TestCity(unittest.TestCase):
    """This is the TestCity class unitest instacne"""

    def test_without_args(self):
        self.assertEqual(City, type(City()))

    def test_with_kwargs(self):
        self.assertEqual(City, type(City(**{})))

    def test_with_None(self):
        self.assertEqual(City, type(City(None)))

    def test_with_id(self):
        self.assertEqual(City, type(City(id="")))

    def test_with_created_at(self):
        self.assertEqual(City, type(City(created_at="")))

    def test_with_updated_at(self):
        self.assertEqual(City, type(City(updated_at="")))

    def test_public_datetime_created_at(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_different_cities_created_at(self):
        ci1 = City()
        sleep(0.1)
        ci2 = City()
        self.assertNotEqual(ci1.created_at, ci2.created_at)

    def test_unused_args(self):
        ci = City(None)
        self.assertNotIn(None, ci.__dict__.values())


if __name__ == "__main__":
    unittest.main()
