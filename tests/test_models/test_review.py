#!/usr/bin/python3
"""
Module test_review
Defines class TestReview
tests class Review
"""


import unittest
import os
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for Review class"""
    @classmethod
    def setUpClass(cls):
        """set up class attributes"""
        cls.rev = Review()
        cls.rev.place_id = "place_id"
        cls.rev.user_id = "user_id"
        cls.rev.text = "text"

    @classmethod
    def tearDownClass(cls):
        del cls.rev
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_Review(self):
        """To test if Review is subclass"""
        self.assertTrue(issubclass(self.rev.__class__, BaseModel), True)

    def test_attributes(self):
        """Tests if attributes are avaliable"""
        self.assertTrue('place_id' in self.rev.__dict__)
        self.assertTrue('user_id' in self.rev.__dict__)
        self.assertTrue('text' in self.rev.__dict__)
        self.assertTrue('id' in self.rev.__dict__)
        self.assertTrue('created_at' in self.rev.__dict__)
        self.assertTrue('updated_at' in self.rev.__dict__)

    def test_attribute_property(self):
        """Test the attribute types"""
        self.assertEqual(type(self.rev.place_id), str)
        self.assertEqual(type(self.rev.user_id), str)
        self.assertEqual(type(self.rev.text), str)

    def test_save(self):
        """tests the save method in Review"""
        self.rev.save()
        self.assertNotEqual(self.rev.created_at, self.rev.updated_at)

    def test_to_dict(self):
        """tests the to_dict method for Review"""
        self.assertEqual("to_dict" in dir(self.rev), True)
