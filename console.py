#!/usr/bin/python3
"""THis module shall contain the console class"""
import cmd
import models
import re
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models import storage
from shlex import split
from os import getenv


class HBNBCommand(cmd.Cmd):
    """This is the console class
    Attributes:
        prompt (str): This represent the prompt
    """
    prompt = '(hbnb) '
    __classes = {
        "BaseModel",
        "User",
        "Place",
        "State",
        "City",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """This will exit the program"""
        return True
    
    def do_EOF(self, arg):
        """This will exit the program"""
        return True
    
    def emptyline(self):
        """This will do nothing"""
        pass

    def do_create(self, arg):
        """This shall create a new instance of BaseModel
        and print the id
        """
        argp = arg.split()
        if len(argp) == 0:
            print("** class name missing **")
        elif argp[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            new = eval(argp[0])()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """This will print the string representation of an instance"""
        argp = arg.split()
        if len(argp) == 0:
            print("** class name missing **")
        elif argp[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(argp) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(argp[0], argp[1])
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """This will print all string representation of all instances"""
        argp = arg.split()
        if len(argp) == 0:
            print([str(v) for v in storage.all().values()])
        elif argp[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            print([str(v) for k, v in storage.all().items() if argp[0] in k])

    def do_update(self, arg):
        """This will update an instance based on the class name and id"""
        argp = split(arg)
        if len(argp) == 0:
            print("** class name missing **")
        elif argp[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(argp) == 1:
            print("** instance id missing **")
        elif len(argp) == 2:
            print("** attribute name missing **")
        elif len(argp) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(argp[0], argp[1])
            if key in storage.all():
                setattr(storage.all()[key], argp[2], argp[3])
                storage.all()[key].save()
            else:
                print("** no instance found **")
