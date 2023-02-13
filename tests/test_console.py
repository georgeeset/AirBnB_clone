#!/usr/bin/python3
"""
unittest module for the console
"""
import unittest
import re
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class TestHBNBCommand(unittest.TestCase):'''
unittests for HBNBCommand class and its methods
'''


