#!/usr/bin/python3
""" class place that inherit from BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ class: place
        Args:
            city_id: the id of the city in string
            user: the user identity
            description: the description of the place in string
            number_rooms: the number of rooms in int.
            other args include: price_by_night, max_guest, latitude, longitude,
                                amenity.
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
