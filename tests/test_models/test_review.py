#!/usr/bin/python3
"""module for testing review class"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """ Test class for review class"""

    def setUp(self):
        """setup test"""
        self.sample = Review()

    def tearDown(self):
        """tear down """
        pass

    def test_instance(self):
        """ confirm the instance of review properties"""
        self.assertEqual(f"{type(self.sample)}",
                         "<class 'models.review.Review'>")
        self.assertIsInstance(self.sample, Review)
        self.assertTrue(issubclass(type(self.sample), BaseModel))

    def test_attributes(self):
        """checks all attributes of class"""
        self.assertIsInstance(self.sample.place_id, str)
        self.assertIsInstance(self.sample.user_id, str)
        self.assertIsInstance(self.sample.text, str)


if __name__ == "__main__":
    unittest.main()
