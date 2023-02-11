#!/usr/bin/python3
"""
Module test_user
Defines class TestUser
tests class User
"""


import unittest
import os
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for User class"""
    @classmethod
    def setUpClass(cls):
        """set up class attributes"""
        cls.user = User()
        cls.user.first_name = "Yoseph"
        cls.user.last_name = "Endale"
        cls.user.email = "endaleyoseph1@gmail.com"
        cls.user.password = "password"

    @classmethod
    def tearDownClass(cls):
        del cls.user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_User(self):
        """To test if User is subclass"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_attributes(self):
        """Tests if attributes are avaliable"""
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)

    def test_first_name(self):
        """test first name"""
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(self.user.first_name, "Yoseph")
        self.assertIsNotNone(self.user.first_name)

    def test_last_name(self):
        """test first name"""
        self.assertEqual(type(self.user.last_name), str)
        self.assertEqual(self.user.last_name, "Endale")
        self.assertIsNotNone(self.user.last_name)

    def test_email(self):
        """test first name"""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(self.user.email, "endaleyoseph1@gmail.com")
        self.assertIsNotNone(self.user.email)

    def test_password(self):
        """test first name"""
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(self.user.password, "password")
        self.assertIsNotNone(self.user.password)

    def test_save(self):
        """tests the save method in User"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict(self):
        """tests the to_dict method for user"""
        self.assertEqual("to_dict" in dir(self.user), True)


if __name__ == "__main__":
    unittest.main()
