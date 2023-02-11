#!/usr/bin/python3
"""
Module user
Defines User class
contains user's infomation
"""


from models.base_model import BaseModel
import json


class User(BaseModel):
    """Inherites from class BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
