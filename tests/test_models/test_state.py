#!/usr/bin/python3
"""module for testing State class"""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """ Test class for State class"""

    def setUp(self):
        """setup test"""
        self.sample = State()

    def tearDown(self):
        """tear down """
        pass

    def test_instance(self):
        """ confirm the instance of state properties"""
        self.assertEqual(f"{type(self.sample)}",
                         "<class 'models.state.State'>")
        self.assertIsInstance(self.sample, State)
        self.assertTrue(issubclass(type(self.sample), BaseModel))

    def test_attributes(self):
        """checks all attributes of class"""
        self.assertIsInstance(self.sample.name, str)


if __name__ == "__main__":
    unittest.main()
