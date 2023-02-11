#!/usr/bin/python3
"""
Module place
Defines Place class
contains places infomation
"""


from models.base_model import BaseModel


class Place(BaseModel):
    """
    Inherites from class BaseModel
    public class attributes:
        city_id(str): it will be the City.id
        user_id(str): it will be the User.id
        name(str): empty string
        description(str): empty string
        number_rooms(int)
        number_bathrooms(int)
        max_guest(int)
        price_by_night(int)
        latitude(float)
        longitude(float)
        amenity_ids(list): list of string
    """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initilizes user"""
        if kwargs:
            for k, v in kwargs.items():
                if not hasattr(BaseModel, k):
                    setattr(self, k, v)
        else:
            super().__init__()
