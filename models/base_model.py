#!/usr/bin/python3
"""
Module base_model
Defines BaseModel class
with public instance attribute
"""


import uuid
import datetime
import models


class BaseModel:
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
        """Initilizes class Base model attributes"""
        if kwargs:
            for k, v in kwargs.items():
                if "created_at" == k:
                    self.created_at = datetime.datetime. \
                                      strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == k:
                    self.updated_at = datetime.datetime. \
                                      strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                elif "__class__" == k:
                    pass
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.today()
            self.updated_at = datetime.datetime.today()
            models.storage.new(self)

    def __str__(self):
        """ print: [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}" \
               .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the current time"""
        self.updated_at = datetime.datetime.today()
        models.storage.save()

    def to_dict(self):
        """converts instances to dictionary"""
        dic = {}
        dic["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if isinstance(v, (datetime.datetime, )):
                dic[k] = v.isoformat()
            else:
                dic[k] = v
        return dic
