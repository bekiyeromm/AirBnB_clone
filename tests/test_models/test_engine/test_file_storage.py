#!/usr/bin/python3
"""
Model file_storage
Define class TestFileStorage
Test FileStorage class
"""


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import unittest
import os


class TestFileStorage(unittest.TestCase):
    """test cases for file_storage"""

    def teardown(Self):
        """tear down an attribute"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """tests all method"""
        storage = FileStorage()
        user = User()
        key = "{}.{}".format(user.__class__.__name__, user.id)
        inst_dic = storage.all()
        self.assertIsInstance(inst_dic, dict)
        self.assertIsNotNone(inst_dic[key])
        self.assertIs(inst_dic, storage._FileStorage__objects)

    def test_new(self):
        """tests new method from FileStorage"""
        storage2 = FileStorage()
        inst_dic = storage2.all()
        user2 = User()
        storage2.new(user2)
        key = user2.__class__.__name__ + "." + user2.id
        self.assertIsNotNone(inst_dic[key])

    def test_reload(self):
        """tests the reload method of FileStorage"""
        storage3 = FileStorage()
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as f:
            for i in f:
                self.assertEqual(i, "{}")
        self.assertIs(storage3.reload(), None)
