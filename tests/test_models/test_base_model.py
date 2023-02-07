#!/usr/bin/python3
'''
series of tests for basemodel class and methods within
'''
import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''
    basemodel tests
    '''
    def setUp(self):
        '''
        sets up some instances to be used for tests
        '''
        self.md1 = BaseModel()
        self.md2 = BaseModel()

    def test_uuid(self):
        '''
        tests if the id is unique for each instance
        '''
        self.assertNotEqual(self.md1.id, self.md2.id)

    def test_init_with_no_args(self):
        '''
        init with no arguments
        '''
        with self.assertRaises(TypeError) as e:
            self.md1 = BaseModel.__init__()
        msg = "BaseModel.__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_is_instance(self):
        '''
        tests if type of attributes is datetime.datetime
        '''
        self.assertIsInstance(self.md1.created_at, datetime.datetime)
        self.assertIsInstance(self.md1.updated_at, datetime.datetime)
        self.assertIsNotNone(self.md1.id)
        self.assertIsNotNone(self.md1.created_at)
        self.assertIsNotNone(self.md1.updated_at)

    def test_str(self):
        '''
        tests if it returns the right string
        '''
        self.assertEqual(self.md1.__str__(), "[{}] ({}) {}".format(self.md1.__class__.__name__, self.md1.id, self.md1.__dict__))

    def test_save(self):
        '''
        tests if the attributes are updated
        '''
        prev_updated_at = self.md1.updated_at
        self.md1.save()
        self.assertNotEqual(prev_updated_at, self.md1.updated_at)

    def test_to_dict(self):
        '''
        tests if it returns a dictionary with the right
        key , value pair
        '''
        todict = self.md1.to_dict()
        self.assertEqual(todict['__class__'], "BaseModel")
        self.assertEqual(todict['created_at'], self.md1.created_at.isoformat())
        self.assertEqual(todict['updated_at'], self.md1.updated_at.isoformat())
        self.assertIsInstance(todict['created_at'].__class__.__name__, str)
        self.assertIsInstance(todict['updated_at'].__class__.__name__, str)

if __name__ == '__main__':
        unittest.main()
