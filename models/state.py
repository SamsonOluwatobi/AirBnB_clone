#!/usr/bin/python3
""" class state that inherits from baseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """
        class: state that inherits from BaseModel
            Args:
                name: the name of the state in string.
    """
    name = ""
