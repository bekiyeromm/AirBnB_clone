#!/usr/bin/python3
"""
Module file_storage
Defines class FileStorage
serialization and deserilization of files
"""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    private class attributes:
        __file_path: string - path to the JSON file
        __objects: dictionary - store all objects

    public methods:
        all(self)
        new(self, obj)
        save(self)
        reload(self)
    """
    __file_path = 'file.json'
    __objects = {}
    class_dic = {"BaseModel": BaseModel, "User": User, "State": State,
                 "City": City, "Amenity": Amenity,
                 "Place": Place, "Review": Review}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        d = {}
        for k, v in self.__objects.items():
            d[k] = v.to_dict()
        with open(self.__file_path, "w") as f:
            f.write(json.dumps(d))

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            d = {}
            with open(self.__file_path) as f:
                d = json.loads(f.read())
            for k, v in d.items():
                obj = self.class_dic[v["__class__"]](**v)
                self.__objects[k] = obj

        except FileNotFoundError:
            pass
