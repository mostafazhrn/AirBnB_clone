#!/usr/bin/python3
"""This shall represent the State class."""
import models
from models.base_model import BaseModel
from os import getenv


class State(BaseModel):
    """This shall represent the state.
    Attributes:
        name (str): rep the name of the state.
    """
    name = ""
