#!/usr/bin/python3
"""
Module amenity
Defines Amenity class
contains Amenity infomation
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Inherites from class BaseModel
    public class attributes:
        name(str): name
    """
    name = ''

    def __init__(self, *args, **kwargs):
        """Initilizes user"""
        if kwargs:
            for k, v in kwargs.items():
                if not hasattr(BaseModel, k):
                    setattr(self, k, v)
        else:
            super().__init__()
