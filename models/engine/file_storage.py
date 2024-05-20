#!/usr/bin/env python3
import json
import os
from models.base_model import BaseModel

"""
Class for storing and retrieving instances of BaseModel to/from a JSON file.
"""


class FileStorage:
    """
    Class for storing and retrieving instances of BaseModel
    to/from a JSON file.

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Dictionary of stored objects.

    Methods:
        all -- Return the dictionary of stored objects.
        new -- Add a new object to the storage.
        save -- Serialize the stored objects to the JSON file.
        reload -- Deserialize the JSON file and update the stored objects.
        __file_exists -- Check if the JSON file exists.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary of stored objects.

        Returns:
            dict: Dictionary of stored objects.
        """
        # If the file exists, deserialize it and return the
        # __objects dictionary
        if self.__file_exists():
            self.reload()
            return self.__objects
        # If the file does not exist, return an empty dictionary
        elif not self.__file_exists():
            return {}
        # Return the __objects dictionary
        return self.__objects

    def new(self, obj):
        """
        Add a new object to the storage.

        Args:
            obj: Instance of BaseModel or subclass.
        """
        # Use the class name and ID as the key
        okey = obj.__class__.__name__
        self.__objects["{}.{}".format(okey, obj.id)] = obj

    def save(self):
        """
        Serialize the stored objects to the JSON file.

        Note:
            This method uses JSON to serialize the dictionary of
            stored objects. The resulting JSON file is written to
            the FileStorage.__file_path attribute.
        """
        keydict = {}
        for key, obj in self.__objects.items():
            if isinstance(obj, BaseModel):
                keydict[key] = obj.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(keydict, f)

    def reload(self):
        """
        Deserialize the JSON file and update the stored objects.

        Note:
            This method reads the JSON file stored at the
            FileStorage.__file_path attribute, deserializes the contents,
            and updates the FileStorage.__objects attribute.
        """
        if self.__file_exists():
            with open(self.__file_path, "r") as f:
                keydict = json.load(f)
                for key, obj_data in keydict.items():
                    cls_name = obj_data["__class__"]
                    if cls_name == "BaseModel":
                        self.new(BaseModel.from_dict(**obj_data))

    def __file_exists(self):
        """
        Check if the JSON file exists.

        Returns:
            bool: True if the file exists, False otherwise.
        """
        return os.path.exists(self.__file_path)
