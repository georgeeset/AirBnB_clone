#!/usr/bin/python3
"""module for testing user class"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ Test class for User model"""

    def setUp(self):
        """setup test"""
        self.sample = User()

    def tearDown(self):
        """tear down """
        pass

    def test_instance(self):
        """ confirm the instance of user properties"""
        self.assertEqual(f"{type(self.sample)}", "<class 'models.user.User'>")
        self.assertIsInstance(self.sample, User)
        self.assertTrue(issubclass(type(self.sample), BaseModel))

    def test_attributes(self):
        """checks all attributes of class"""
        self.assertIsInstance(self.sample.email, str)
        self.assertIsInstance(self.sample.password, str)
        self.assertIsInstance(self.sample.first_name, str)
        self.assertIsInstance(self.sample.last_name, str)


if __name__ == "__main__":
    unittest.main()
