#!/usr/bin/python3
"""
This module shall contain the User class
"""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5


class User(BaseModel):
    """This is the User class
    Attributes:
        email (str): This represent the email
        password (str): This represent the password
        first_name (str): This represent the first name
        last_name (str): This represent the last name
    """
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    def __init__(self, *args, **kwargs):
        """This shall start the User class"""
        super().__init__(*args, **kwargs)
        self.password = md5(self.password.encode()).hexdigest()

    def __setattr__(self, name, value):
        """This shall set the password"""
        if name == 'password':
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
