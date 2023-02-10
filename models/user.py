#!/usr/bin/python3
"""
Module user
Defines User class
contains user's infomation
"""


from models.base_model import BaseModel
import datetime


class User(BaseModel):
    """
    Inherites from class BaseModel
    public class attributes:
        email(str): user email address
        password(str): user password
        first_name(str): user first name
        last_name(str): user last name
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """Initilizes user"""
        if kwargs:
            for k, v in kwargs.items():
                if not hasattr(BaseModel, k):
                    setattr(self, k, v)
        else:
            super().__init__()
