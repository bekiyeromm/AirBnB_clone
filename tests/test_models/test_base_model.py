#!/usr/bin/python3
"""
Module test_base_model
Defines class TestBaseModel
tests the base_model
"""


import unittest
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Testcase for BaseModel class
    """
    def setUp(self):
        """set up an attribute"""
        self.model = BaseModel()
        self.model.name = "jack"

    def tearDown(self):
        """tear down an attribute"""
        del self.model
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_documentation(self):
        """tests documentation of base_model"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_base_model_attr(self):
        """tests the attributes of the class"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_instances(self):
        """test if an instance is a BaseModel"""
        self.assertTrue(isinstance(self.model, BaseModel))

    def test_save(self):
        """tests the save method of basemodel"""
        self.model.save()
        self.assertNotEqual(self.model.created_at, self.model.updated_at)

    def test_to_dict(self):
        dic = self.model.to_dict()
        self.assertEqual(dic["__class__"], "BaseModel")
        self.assertIsInstance(dic["created_at"], str)
        self.assertIsInstance(dic["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
