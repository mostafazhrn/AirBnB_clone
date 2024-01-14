#!/usr/bin/python3
"""This module shall contain the console class"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from datetime import datetime
import shlex

clsses = {"BaseModel": BaseModel, "User": User, "Place": Place,
          "State": State, "City": City, "Review": Review,
          "Amenity": Amenity}


class HBNBCommand(cmd.Cmd):
    """This is the HBNBCommand class
    Attributes:
        prompt (str): This represent the prompt
    """
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """This shall exit the program"""
        return True

    def do_EOF(self, arg):
        """This shall exit the program"""
        return True

    def emptyline(self):
        """This shall do nothing"""
        pass

    def do_create(self, arg):
        """This shall create a new instance of BaseModel,
        save it (to the JSON file) and prints the id"""
        arg_pls = arg.split()
        if len(arg_pls) == 0:
            print("** class name missing **")
        elif arg_pls[0] not in clsses:
            print("** class doesn't exist **")
        else:
            new = clsses[arg_pls[0]]()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """This shall print the string representation of an instance
        based on the class name and id"""
        arg_pls = arg.split()
        if len(arg_pls) == 0:
            print("** class name missing **")
        elif arg_pls[0] not in clsses:
            print("** class doesn't exist **")
        elif len(arg_pls) == 1:
            print("** instance id missing **")
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """This shall delete an instance based on the class name and id"""
        arg_pls = arg.split()
        if len(arg_pls) == 0:
            print("** class name missing **")
        elif arg_pls[0] not in clsses:
            print("** class doesn't exist **")
        elif len(arg_pls) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg_pls[0], arg_pls[1])
            if key in models.storage.all():
                del models.storage.all()[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """This shall print all string representation of all instances
        based or not on the class name"""
        arg_pls = arg.split()
        if len(arg_pls) == 0:
            print([str(v) for v in models.storage.all().values()])
        elif arg_pls[0] not in clsses:
            print("** class doesn't exist **")
        else:
            print([str(v) for k, v in models.storage.all().items()
                   if k.split('.')[0] == arg_pls[0]])

    def do_update(self, arg):
        """This shall update an instance based on the class name and id
        by adding or updating attribute"""
        arg_pls = shlex.split(arg)
        if len(arg_pls) == 0:
            print("** class name missing **")
        elif arg_pls[0] not in clsses:
            print("** class doesn't exist **")
        elif len(arg_pls) == 1:
            print("** instance id missing **")
        elif len(arg_pls) == 2:
            print("** attribute name missing **")
        elif len(arg_pls) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(arg_pls[0], arg_pls[1])
            if key in models.storage.all():
                obj = models.storage.all()[key]
                setattr(obj, arg_pls[2], arg_pls[3])
                obj.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
