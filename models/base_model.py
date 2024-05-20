#!/usr/bin/env python3
import json
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Base class for all models.

    This class provides the basic attributes and methods for all models.

    Attributes:
        id (str): Unique identifier of the instance
        created_at (datetime): Timestamp when the instance was created
        updated_at (datetime): Timestamp when the instance was last updated

    Methods:
        __init__ -- Initialize a new BaseModel instance
        __str__ -- Return a string representation of the instance
        to_dict -- Return a dictionary representation of the instance
        from_dict -- Create a new BaseModel instance from a dictionary
        representation save -- Update the updated_at attribute with the
        current datetime and save to file
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.

        Args:
            *args: Arbitrary positional arguments (not used).
            **kwargs: Arbitrary keyword arguments to set as attributes.

        This method initializes a new BaseModel instance.
        It sets the id attribute to a random UUID,
        the created_at and updated_at attributes to the current datetime,
        and accepts arbitrary keyword arguments to set additional attributes.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for k, v in kwargs.items():
                if k in ["created_at", "updated_at"]:
                    if isinstance(v, str):
                        self.__dict__[k] = datetime.fromisoformat(v)
                    else:
                        self.__dict__[k] = v
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """
        Return a string representation of the BaseModel instance.

        Returns:
            str: A string representation of the instance.
        """
        # Use f-string to format the string representation
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """
        Return a dictionary representation of the instance.

        Returns:
            dict: A dictionary representation of the instance.

        This method returns a dictionary that includes all attributes
        of the instance, including the class name, created_at, and updated_at
        converted to strings in ISO format.
        """
        # Use vars() to get the instance's dictionary
        obj_dict = vars(self)
        # Add a key "__class__" with the class name of the object
        obj_dict["__class__"] = self.__class__.__name__
        # Convert created_at and updated_at to strings in ISO format
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

    @classmethod
    def from_dict(cls, **kwargs):
        """
        Create a new BaseModel instance from a dictionary representation.

        Args:
            **kwargs: Dictionary representation of a BaseModel instance.

        Returns:
            BaseModel: A new BaseModel instance created from the dictionary.

        This method creates a new BaseModel instance by setting its attributes
        from the provided dictionary. It converts the created_at and updated_at
        values from strings to datetime objects.
        """
        if isinstance(kwargs["created_at"], str):
            kwargs["created_at"] = datetime.fromisoformat(kwargs["created_at"])
        if isinstance(kwargs["updated_at"], str):
            kwargs["updated_at"] = datetime.fromisoformat(kwargs["updated_at"])
        return cls(**kwargs)

    def save(self):
        """
        Update the updated_at attribute with the current datetime and save
        to file.

        This method updates the updated_at attribute with the current datetime
        and saves the object to the storage system.
        """
        self.updated_at = datetime.now()
        models.storage.new(self)  # Ensure the object is added to storage
        models.storage.save()
