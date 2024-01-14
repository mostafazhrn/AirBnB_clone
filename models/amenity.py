#!/usr/bin/python3
"""This shall define the Amenity class."""
import models
from models.base_model import BaseModel
from os import getenv


class Amenity(BaseModel):
    """This shall represent an amenity.
    Attributes:
        name (str): This rep name of the amenity.
    """
    name = ""
