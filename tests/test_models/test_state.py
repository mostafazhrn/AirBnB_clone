#!/usr/bin/python3
"""This module shall contain the unittests for state.py"""
import unittest
import models
import os
from datetime import datetime
from time import sleep
from models.state import State


class TestState(unittest.TestCase):
    """This is the TestState class unitest instacne"""

    def test_without_args(self):
        self.assertEqual(State, type(State()))

    def test_with_kwargs(self):
        self.assertEqual(State, type(State(**{})))

    def test_with_None(self):
        self.assertEqual(State, type(State(None)))

    def test_with_id(self):
        self.assertEqual(State, type(State(id="")))

    def test_with_created_at(self):
        self.assertEqual(State, type(State(created_at="")))

    def test_with_updated_at(self):
        self.assertEqual(State, type(State(updated_at="")))

    def test_public_datetime_created_at(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_different_states_created_at(self):
        s1 = State()
        sleep(0.1)
        s2 = State()
        self.assertNotEqual(s1.created_at, s2.created_at)

    def test_unused_args(self):
        s = State(None)
        self.assertNotIn(None, s.__dict__.values())


if __name__ == "__main__":
    unittest.main()
