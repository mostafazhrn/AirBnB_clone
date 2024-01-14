#!/usr/bin/python3
"""This module shall contain the unittests for review.py"""
import unittest
import models
import os
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview(unittest.TestCase):
    """This is the TestReview class unitest instacne"""

    def test_without_args(self):
        self.assertEqual(Review, type(Review()))

    def test_with_kwargs(self):
        self.assertEqual(Review, type(Review(**{})))

    def test_with_None(self):
        self.assertEqual(Review, type(Review(None)))

    def test_with_id(self):
        self.assertEqual(Review, type(Review(id="")))

    def test_with_created_at(self):
        self.assertEqual(Review, type(Review(created_at="")))

    def test_with_updated_at(self):
        self.assertEqual(Review, type(Review(updated_at="")))

    def test_public_datetime_created_at(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_different_reviews_created_at(self):
        r1 = Review()
        sleep(0.1)
        r2 = Review()
        self.assertNotEqual(r1.created_at, r2.created_at)

    def test_unused_args(self):
        r = Review(None)
        self.assertNotIn(None, r.__dict__.values())


if __name__ == "__main__":
    unittest.main()
