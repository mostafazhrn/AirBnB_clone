#!/usr/bin/python3
"""This module shall contain the unittests for user.py"""
import unittest
import models
import os
from datetime import datetime
from time import sleep
from models.user import User


class TestUser(unittest.TestCase):
    """This is the TestUser class unitest instacne"""

    def test_without_args(self):
        self.assertEqual(User, type(User()))

    def test_with_kwargs(self):
        self.assertEqual(User, type(User(**{})))

    def test_with_None(self):
        self.assertEqual(User, type(User(None)))

    def test_with_id(self):
        self.assertEqual(User, type(User(id="")))

    def test_with_created_at(self):
        self.assertEqual(User, type(User(created_at="")))

    def test_with_updated_at(self):
        self.assertEqual(User, type(User(updated_at="")))

    def test_public_datetime_created_at(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_different_users_created_at(self):
        u1 = User()
        sleep(0.1)
        u2 = User()
        self.assertNotEqual(u1.created_at, u2.created_at)

    def test_unused_args(self):
        u = User(None)
        self.assertNotIn(None, u.__dict__.values())


if __name__ == "__main__":
    unittest.main()
