#!/usr/bin/python3
"""
Module test_state
Defines class TestState
tests class State
"""


import unittest
import os
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for State class"""
    @classmethod
    def setUpClass(cls):
        """set up class attributes"""
        cls.state = State()
        cls.state.name = "Addis Ababa"

    @classmethod
    def tearDownClass(cls):
        del cls.state
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_State(self):
        """To test if State is subclass"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_attributes(self):
        """Tests if attributes are avaliable"""
        self.assertTrue('name' in self.state.__dict__)
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)

    def test_attribute_property(self):
        """Tests attribute types"""
        self.assertEqual(type(self.state.name), str)

    def test_save(self):
        """tests the save method in State"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict(self):
        """tests the to_dict method for State"""
        self.assertEqual("to_dict" in dir(self.state), True)
