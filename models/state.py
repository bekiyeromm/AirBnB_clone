#!/usr/bin/python3
"""
Module state
Defines User class
contains state's infomation
"""


from models.base_model import BaseModel


class State(BaseModel):
    """
    Inherites from class BaseModel
    public class attributes:
        name(str): state name
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
