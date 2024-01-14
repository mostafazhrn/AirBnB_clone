#!/usr/bin/python3
"""
This module shall contain the User class
"""
import models
from models.base_model import BaseModel
from os import getenv


class User(BaseModel):
    """This is the User class
    Attributes:
        email (str): This represent the email
        password (str): This represent the password
        first_name (str): This represent the first name
        last_name (str): This represent the last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
