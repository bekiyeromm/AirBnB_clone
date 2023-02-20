#!/usr/bin/python3
"""
Module review
Defines Review class
contains review's infomation
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    Inherites from class BaseModel
    public class attributes:
        place_id(str): empty string: it will be the Place.id
        user_id(str): empty string: it will be the User.id
        text(str): empty string
    """
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """Initilizes user"""
        if kwargs:
            for k, v in kwargs.items():
                if not hasattr(BaseModel, k):
                    setattr(self, k, v)
        else:
            super().__init__()
