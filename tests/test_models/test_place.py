#!/usr/bin/python3
"""module for tests on Place class"""

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """test place class"""

    def setUp(self):
        """set up"""
        self.sample = Place()

    def tearDown(self):
        """tear down"""
        pass

    def test_instance(self):
        """ test the instance of Place class"""
        self.assertEqual(f"{type(self.sample)}",
                         "<class 'models.place.Place'>")
        self.assertIsInstance(self.sample, Place)
        self.assertTrue(issubclass(type(self.sample), BaseModel))

    def test_attribute(self):
        """ Test attribute of Place class"""
        self.assertIsInstance(self.sample.city_id, str)
        self.assertIsInstance(self.sample.user_id, str)
        self.assertIsInstance(self.sample.name, str)
        self.assertIsInstance(self.sample.description, str)
        self.assertIsInstance(self.sample.number_rooms, int)
        self.assertIsInstance(self.sample.number_bathrooms, int)
        self.assertIsInstance(self.sample.max_guest, int)
        self.assertIsInstance(self.sample.price_by_night, int)
        self.assertIsInstance(self.sample.latitude, float)
        self.assertIsInstance(self.sample.longitude, float)
        self.assertIsInstance(self.sample.amenity_ids, list)

    def test_default_values(self):
        """ Default value of class attribute"""
        self.assertTrue(self.sample.city_id == "")
        self.assertTrue(self.sample.user_id == "")
        self.assertTrue(self.sample.name == "")
        self.assertTrue(self.sample.description == "")
        self.assertTrue(self.sample.number_rooms == 0)
        self.assertTrue(self.sample.number_bathrooms == 0)
        self.assertTrue(self.sample.max_guest == 0)
        self.assertTrue(self.sample.price_by_night == 0)
        self.assertTrue(self.sample.latitude == 0.0)
        self.assertTrue(self.sample.longitude == 0.0)
        self.assertTrue(self.sample.amenity_ids == [])


if __name__ == "__main__":
    unittest.main()
