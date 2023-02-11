#!/usr/bin/python3
"""
Module city
Defines City class
contains user's infomation
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    Inherites from class BaseModel
    public class attributes:
        name(str): city name
        state_id(str): state id
    """
    name = ''
    state_id = ''

    def __init__(self, *args, **kwargs):
        """Initilizes user"""
        if kwargs:
            for k, v in kwargs.items():
                if not hasattr(BaseModel, k):
                    setattr(self, k, v)
        else:
            super().__init__()
