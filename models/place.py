#!/usr/bin/python3
"""
This module shall contain the Place class
"""
import models
from models.base_model import BaseModel
from os import getenv


class Place(BaseModel):
    """This is the Place class
    Attributes:
        city_id (str): This represent the city id
        user_id (str): This represent the user id
        name (str): This represent the name
        description (str): This represent the description
        number_rooms (int): This represent the number of rooms
        number_bathrooms (int): This represent the number of bathrooms
        max_guest (int): This represent the max guest
        price_by_night (int): This represent the price by night
        latitude (float): This represent the latitude
        longitude (float): This represent the longitude
        amenity_ids (list): This represent the amenity ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
