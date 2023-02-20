#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models

"""
Module base_model
Defines BaseModel class
with public instance attribute
"""


class BaseModel():
    """
    Base model for the drived classes
    attributes:
        id(str): assign with an uuid
        created_at: datetime-assign with current datetime
        updated_at: datetime-assign with current datetime
    Methods:
        __str__(self): should print the info about class
        save(self): updates the public instance attribute updated_at
        to_dict(self):  returns a dictionary containing all keys/values
    """
    def __init__(self, *args, **kwargs):
        """
        Initilizes class Base model attributes


        """
        if kwargs:
            for k, v in kwargs.items():
                if "created_at" == k:
                    self.created_at = datetime. \
                                      strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == k:
                    self.updated_at = datetime. \
                                      strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                elif "__class__" == k:
                    pass
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ print: [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}" \
               .format(self.__class__.__name__, self.id, self.__dict__)

    def __repr__(self):
        """Returns string representation"""
        return (self.__str__())

    def save(self):
        """Updates the current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """converts instances to dictionary"""
        dic = {}
        dic["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if isinstance(v, (datetime, )):
                dic[k] = v.isoformat()
            else:
                dic[k] = v
        return dic
