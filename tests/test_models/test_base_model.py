#!/usr/bin/python3
'''
series of tests for basemodel class and methods within
'''
import unittest
import datetime
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


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

    def tearDown(self):
        '''
        Tear down pocedure
        Remove saved files after test
        '''
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_uuid(self):
        '''
        tests if the id is unique for each instance
        '''
        self.assertNotEqual(self.md1.id, self.md2.id)
        self.assertEqual(len(f"{self.md1.id}"), len(f"{self.md2.id}"))

    def test_init_with_no_args(self):
        '''
        init with no arguments
        '''
        with self.assertRaises(TypeError) as e:
            self.md1 = BaseModel.__init__()

    def test_is_instance(self):
        '''
        tests if type of attributes is datetime.datetime
        '''
        self.assertIsInstance(self.md1.created_at, datetime.datetime)
        self.assertIsInstance(self.md1.updated_at, datetime.datetime)
        self.assertIsNotNone(self.md1.id)
        self.assertIsNotNone(self.md1.created_at)
        self.assertIsNotNone(self.md1.updated_at)

    def test_date_time(self):
        '''
        check if datetime is correct
        '''
        test_class = BaseModel()
        date = datetime.datetime.now()
        difference = test_class.updated_at - test_class.created_at
        self.assertTrue(abs(difference.total_seconds()) < 0.01)
        difference = test_class.created_at - date
        self.assertTrue(abs(difference.total_seconds()) < 0.1)

    def test_time_format(self):
        '''
        test that confirms the time format
        '''
        self.md1.save()
        md1_json = self.md1.to_dict()
        update = self.md1.updated_at
        confirmation = datetime.datetime.strptime(md1_json["updated_at"],
                                                  "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(update, confirmation)

    def test_str(self):
        '''
        tests if it returns the right string
        '''
        self.assertEqual(
            self.md1.__str__(),
            "[{}] ({}) {}".format(
                self.md1.__class__.__name__,
                self.md1.id, self.md1.__dict__
            )
        )

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
