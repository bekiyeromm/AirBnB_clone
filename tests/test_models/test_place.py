#!/usr/bin/python3
"""
Module test_place
Defines class TestPlace
tests class Place
"""


import unittest
import os
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for Place class"""
    @classmethod
    def setUpClass(cls):
        """set up class attributes"""
        cls.place = Place()
        cls.place.city_id = "city.id"
        cls.place.user_id = "user.id"
        cls.place.name = "Place name"
        cls.place.description = "description for the place"
        cls.place.number_rooms = 3
        cls.place.number_bathrooms = 1
        cls.place.max_guest = 4
        cls.place.price_by_night = 200
        cls.place.latitude = 8.9806
        cls.place.longitude = 38.7578
        cls.place.amenity_ids = "amenity ids"

    @classmethod
    def tearDownClass(cls):
        del cls.place
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_Place(self):
        """To test if Place is subclass"""
        self.assertTrue(issubclass(self.place.__class__, BaseModel), True)

    def test_attributes(self):
        """Tests if attributes are avaliable"""
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('number_rooms' in self.place.__dict__)
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)

    def test_attribute_property(self):
        """Tests attribute types"""
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.latitude), float)

    def test_save(self):
        """tests the save method in User"""
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_to_dict(self):
        """tests the to_dict method for user"""
        self.assertEqual("to_dict" in dir(self.place), True)
