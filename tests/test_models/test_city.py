#!/usr/bin/python3
"""test module for city class"""

import unittest
from models.city import City
from models.base_model import BaseModel


class Test_City(unittest.TestCase):
    """ test class for city"""
    def setUp(self):
        """set up"""
        self.sample = City()

    def tearDown(self):
        """tear down"""
        pass

    def test_instance(self):
        """ test the instance of City class"""
        self.assertEqual(f"{type(self.sample)}",
                         "<class 'models.city.City'>")
        self.assertIsInstance(self.sample, City)
        self.assertTrue(issubclass(type(self.sample), BaseModel))

    def test_attribute(self):
        """ Test attribute of City class"""
        self.assertIsInstance(self.sample.state_id, str)
        self.assertIsInstance(self.sample.name, str)

    def test_default_values(self):
        """ Default value of class attribute"""
        self.assertTrue(self.sample.state_id == "")
        self.assertTrue(self.sample.name == "")


if __name__ == "__main__":
    unittest.main()
