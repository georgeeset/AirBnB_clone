#!/usr/bin/python3
"""test module for Amenity class"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class Test_Amenity(unittest.TestCase):
    """ test class for Amenity"""

    def setUp(self):
        """set up"""
        self.sample = Amenity()

    def tearDown(self):
        """tear down"""
        pass

    def test_instance(self):
        """ test the instance of Amenity class"""
        self.assertEqual(f"{type(self.sample)}",
                         "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(self.sample, Amenity)
        self.assertTrue(issubclass(type(self.sample), BaseModel))

    def test_attribute(self):
        """ Test attribute of Amenity class"""
        self.assertIsInstance(self.sample.name, str)

    def test_default_values(self):
        """ Default value of class attribute"""
        self.assertTrue(self.sample.name == "")


if __name__ == "__main__":
    unittest.main()
