#!/usr/bin/python3
"""This shall represent the City class."""
import models
from models.base_model import BaseModel
from os import getenv


class City(BaseModel):
    """This shall represent a city.
    Attributes:
        state_id (str): This represent  state id.
        name (str): This represent name of city.
    """
    state_id = ""
    name = ""
