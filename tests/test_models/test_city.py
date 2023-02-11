#!/usr/bin/python3
"""
Module test_city
Defines class TestCity
tests class City
"""


import unittest
import os
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for User class"""
    @classmethod
    def setUpClass(cls):
        """set up class attributes"""
        cls.city = City()
        cls.city.state_id = "state_id"
        cls.city.name = "Addis Ababa"

    @classmethod
    def tearDownClass(cls):
        del cls.city
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_City(self):
        """To test if City is subclass"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_attributes(self):
        """Tests if attributes are avaliable"""
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)

    def test_attribute_property(self):
        """Tests attribute types"""
        self.assertEqual(type(self.city.state_id), str)
        self.assertEqual(type(self.city.name), str)

    def test_save(self):
        """tests the save method in City"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict(self):
        """tests the to_dict method for City"""
        self.assertEqual("to_dict" in dir(self.city), True)
