#!/usr/bin/env python3
import unittest
from datetime import datetime
from models.base_model import BaseModel


"""
Test module for the BaseModel class

This module contains unit tests for the BaseModel class.

"""


class TestBaseModel(unittest.TestCase):
    """
    Test class for the BaseModel class.

    This class contains unit tests for the BaseModel class.

    """

    def test_init(self):
        """
        Test the __init__ method of the BaseModel class.

        This test case verifies that the id, created_at, and updated_at
        attributes are correctly initialized when an instance of the
        BaseModel class is created.

        """
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_save(self):
        """
        Test the save method of the BaseModel class.

        This test case verifies that the updated_at attribute is updated
        when the save method is called on an instance of the BaseModel
        class.

        """
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, original_updated_at)

    def test_save_edge_case(self):
        """
        Test the save method of the BaseModel class in an edge case.

        This test case verifies that the updated_at attribute is updated
        when the save method is called on an instance of the BaseModel
        class, even if the instance has already been saved.

        """
        model = BaseModel()
        model.save()
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, original_updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of the BaseModel class.

        This test case verifies that the to_dict method returns a dictionary
        that includes all attributes of the instance, including the class
        name, created_at, and updated_at converted to strings in ISO format.

        """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["id"], model.id)
        self.assertEqual(model_dict["__class__"], "BaseModel")

    def test_to_dict_edge_case(self):
        """
        Test the to_dict method of the BaseModel class in an edge case.

        This test case verifies that the to_dict method returns a dictionary
        that includes all attributes of the instance, including the class
        name, created_at, and updated_at converted to strings in ISO format,
        even if the instance has no id.

        """
        model = BaseModel()
        model.id = None
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["id"], None)
        self.assertEqual(model_dict["__class__"], "BaseModel")
