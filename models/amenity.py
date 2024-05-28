#!/usr/bin/python3
""" class Amenities that inherit from BaseMOdel """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ class: Amenity.
        Args:
            name: the name in string
    """
    name = ""
