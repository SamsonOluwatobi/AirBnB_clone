#!/usr/bin/python3
""" class review that that inherit from basemodel """
from models.base_model import BaseModel


class Review(BaseModel):
    """
        class : Represents a review associated with a place
        Args: BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
