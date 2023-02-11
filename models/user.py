#!/usr/bin/python3
"""
Module user
Defines User class
contains user's infomation
"""


from models.base_model import BaseModel
import json


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
