#!/usr/bin/python3
"""
This module shall contain the Review class
"""
import models
from models.base_model import BaseModel
from os import getenv


class Review(BaseModel):
    """This is the Review class
    Attributes:
        place_id (str): This represent the place id
        user_id (str): This represent the user id
        text (str): This represent the text
    """
    place_id = ""
    user_id = ""
    text = ""
