#!/usr/bin/python3
'''
series of tests for basemodel class and methods within
'''
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''
    basemodel tests
    '''
    def setUp(self):
        '''
        sets up some instances to be used for tests
        '''
        md1 = BaseModel()
        md2 = BaseModel()

    def test_uuid(self):
        '''
        tests if the id is unique for each instance
        '''
        assertNotEqual(md1.id, md2.id)

    def test_is_instance(self):
        '''
        tests if type of attributes is datetime.datetime
        '''
        assertIsInstance(md1.created_at.__class__.__name__, datetime.datetime)
        assertIsInstance(md1.updated_at.__class__.__name__, datetime.datetime)

    def test_str(self):
        '''
        tests if it returns the right string
        '''
        assertEqual(md1.__str__, "[{}] ({}) {}".format((self.__class__.__name__),
                                             self.id, self.__dict__))

    def test_save(self):
        '''
        tests if the attributes are updated
        '''
        prev_update_at = md1.updated_at
        md1.save()
        self.assertNotEqual(prev_updated_at, md1.updated_at)

    def test_to_dict(self):
        '''
        tests if it returns a dictionary with the right
        key , value pair
        '''
        todict = md1.to_dict()
        assertEqual(todict[__class__], "BaseModel")
        assertEqual(todict[created_at], md1.created_at.isoformat())
        assertEqual(todict[updated_at], md1.updated_at.isoformat())
        assertIsInstance(todict[created_at].__class__.__name__, str)
        assertIsInstance(todict[updated_at].__class__.__name__, str)

if __name__ == '__main__':
        unittest.main()
