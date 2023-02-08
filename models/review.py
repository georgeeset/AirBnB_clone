#!/usr/bin/python3
""" Review Class Module """
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class extending BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
