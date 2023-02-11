#!/usr/bin/python3
"""
Contains the subclass City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ creates an instance of a city """

    state_id = ""
    name = ""
