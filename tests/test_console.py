#!/usr/bin/python3
"""This module shall contain the unittests for console.py"""
import unittest
import os
import models
import sys
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """This is the TestConsole class
    Attributes:
        clsdict (dict): This represent the dictionary of classes
        clsnames (list): This represent the list of class names
        clsobjs (list): This represent the list of class objects
        clsdict (dict): This represent the dictionary of classes
    """
    def setUp(self):
        """This shall set up the environment for testing"""
        self.clsdict = {"BaseModel": BaseModel}
        self.clsnames = ["BaseModel"]
        self.clsobjs = [BaseModel]
        self.console = HBNBCommand()

    def tearDown(self):
        """This shall tear down the environment for testing"""
        if os.path.isfile("file.json"):
            os.remove("file.json")

    def test_docstrings(self):
        """This shall test the docstrings"""
        self.assertIsNotNone(console.__doc__
                             and console.HBNBCommand.__doc__
                             and console.HBNBCommand.do_quit.__doc__
                             and console.HBNBCommand.do_EOF.__doc__
                             and console.HBNBCommand.emptyline.__doc__
                             and console.HBNBCommand.do_create.__doc__
                             and console.HBNBCommand.do_show.__doc__
                             and console.HBNBCommand.do_destroy.__doc__
                             and console.HBNBCommand.do_all.__doc__
                             and console.HBNBCommand.do_update.__doc__)

    def test_create(self):
        """This shall test the create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create MyModel")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        for i in range(len(self.clsnames)):
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd("create {}".format(self.clsnames[i]))
                self.assertTrue(len(f.getvalue()) > 0)
                self.assertTrue(f.getvalue()[-1] == '\n')
                self.assertTrue(f.getvalue()[:-1].isalnum())
                self.assertTrue(f.getvalue()[:-1] in models.storage.all())
                self.assertTrue(type(models.storage.
                                     all()[f.getvalue()[:-1]]) ==
                                self.clsobjs[i])

    def test_show(self):
        """This shall test the show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show MyModel")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel 123")
            self.assertEqual(f.getvalue(), "** no instance found **\n")
        new = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel {}".format(new.id))
            self.assertEqual(f.getvalue(), str(new) + '\n')


if __name__ == "__main__":
    unittest.main()
