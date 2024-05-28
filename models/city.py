#!/usr/bin/python3
""" class city that inherits from basModel """
from models.base_model import BaseModel


class City(BaseModel):
    """
        class: Represent a city with a name
        Arg:
            state_id: the state id in string
            name: the name of the city in string
    """
    state_id = ""
    name = ""
