#!/usr/bin/python3
""" User that inherits from BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ User that inherits from BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """construct for the class user"""
        super().__init__(*args, **kwargs)
