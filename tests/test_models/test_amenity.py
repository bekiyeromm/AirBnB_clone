#!/usr/bin/python3
"""
Module test_amenity
Defines class TestAmenity
tests class User
"""


import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""
    @classmethod
    def setUpClass(cls):
        """set up class attributes"""
        cls.room = Amenity()
        cls.room.name = "room"

    @classmethod
    def tearDownClass(cls):
        del cls.room
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_Amenity(self):
        """To test if Amenity is subclass"""
        self.assertTrue(issubclass(self.room.__class__, BaseModel), True)

    def test_attributes(self):
        """Tests if attributes are avaliable"""
        self.assertTrue('name' in self.room.__dict__)
        self.assertTrue('id' in self.room.__dict__)
        self.assertTrue('created_at' in self.room.__dict__)
        self.assertTrue('updated_at' in self.room.__dict__)

    def test_attribute_property(self):
        """Tests attribute types"""
        self.assertEqual(type(self.room.name), str)

    def test_save(self):
        """tests the save method in Amenity"""
        self.room.save()
        self.assertNotEqual(self.room.created_at, self.room.updated_at)

    def test_to_dict(self):
        """tests the to_dict method for Amenity"""
        self.assertEqual("to_dict" in dir(self.room), True)
