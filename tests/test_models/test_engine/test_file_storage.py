#!/usr/bin/env python3
"""
test m;odule for FileStorage class
"""
import unittest
from datetime import datetime
import time
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.user import User
import os
import json


class TestFileStorage(unittest.TestCase):
    """
    Test class for File storage class
    """

    def removeFiles(self):
        """ remove files for clean start"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def setUp(self):
        """ Setup method"""
        pass

    def tearDown(self):
        """ teardown method"""
        self.removeFiles()

    def test_init_with_args(self):
        """parse args to file storage"""
        with self.assertRaises(TypeError) as err:
            instvalue = FileStorage(1, 2, 3)
        msg = "FileStorage() takes no arguments"
        self.assertEqual(str(err.exception), msg)

    def test_class_attr(self):
        """test all attributes of FileStorage Class"""
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))

    """================Test method AlL with Existing classes"""
    def prepare_all_test(self, test_class):
        """Prepare each class for the test"""
        storage.new(test_class)
        key = "{}.{}".format(type(test_class).__name__, test_class.id)
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], test_class)

    def test_all_base(self):
        """test the all method using BaseModel"""
        self.assertEqual(storage.all(), {})
        self.prepare_all_test(BaseModel())

    def test_all_user(self):
        """test the all method using BaseModel"""
        self.assertEqual(storage.all(), {})
        self.prepare_all_test(User())

    def test_all_city(self):
        """test the all method using BaseModel"""
        self.assertEqual(storage.all(), {})
        self.prepare_all_test(City())

    def test_all_state(self):
        """test the all method using BaseModel"""
        self.assertEqual(storage.all(), {})
        self.prepare_all_test(State())

    def test_all_review(self):
        """test the all method using BaseModel"""
        self.assertEqual(storage.all(), {})
        self.prepare_all_test(Review())

    def test_all_amenity(self):
        """test the all method using BaseModel"""
        self.assertEqual(storage.all(), {})
        self.prepare_all_test(Amenity())

    def test_all_place(self):
        """test the all method using BaseModel"""
        self.assertEqual(storage.all(), {})
        self.prepare_all_test(Place())

    def test_all_with_no_args(self):
        """test all method without arguments"""
        with self.assertRaises(TypeError) as e:
            FileStorage.all()
        msg = ("FileStorage.all() missing 1 required "
               "positional argument: 'self'")
        self.assertEqual(str(e.exception), msg)

    """====Test The New method in storage class with available models ======"""

    def prepare_new_test(self, test_class):
        """ Prepare class proparty for all models"""
        cls = test_class
        storage.new(cls)
        key = "{}.{}".format(type(cls).__name__, cls.id)
        self.assertTrue(key in FileStorage._FileStorage__objects)
        self.assertEqual(FileStorage._FileStorage__objects[key], cls)

    def test_new_base(self):
        """ test the new method with new BaseModel"""
        self.prepare_new_test(BaseModel())

    def test_new_User(self):
        """ test the new method with new BaseModel"""
        self.prepare_new_test(User())

    def test_new_state(self):
        """ test the new method with new BaseModel"""
        self.prepare_new_test(State())

    def test_new_place(self):
        """ test the new method with new BaseModel"""
        self.prepare_new_test(Place())

    def test_new_review(self):
        """ test the new method with new BaseModel"""
        self.prepare_new_test(Review())

    def test_new_amenity(self):
        """ test the new method with new BaseModel"""
        self.prepare_new_test(Amenity())

    def test_new_city(self):
        """ test the new method with new BaseModel"""
        self.prepare_new_test(City())

    """=========Test Save method with all available models"""
    def prepare_save_test(self, test_class):
        """prepare test for save method"""
        storage.new(test_class)
        key = "{}.{}".format(type(test_class).__name__, test_class.id)
        storage.save()
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        rep = {key: test_class.to_dict()}
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(rep)))
            f.seek(0)
            self.assertEqual(json.load(f), rep)

    def test_save_base(self):
        """ test the save method with BaseModel"""
        self.prepare_save_test(BaseModel())

    def test_save_user(self):
        """ test the save method with BaseModel"""
        self.prepare_save_test(User())

    def test_save_place(self):
        """ test the save method with BaseModel"""
        self.prepare_save_test(Place())

    def test_save_state(self):
        """ test the save method with BaseModel"""
        self.prepare_save_test(State())

    def test_save_amenity(self):
        """ test the save method with BaseModel"""
        self.prepare_save_test(Amenity())

    def test_save_city(self):
        """ test the save method with BaseModel"""
        self.prepare_save_test(City())

    def test_save_review(self):
        """ test the save method with BaseModel"""
        self.prepare_save_test(Review())

    """==============Test Reload method with all models=============="""
    def prepare_reload_test(self, class_name):
        """PREPARE reload test for all calsses"""
        storage.reload()
        self.assertEqual(FileStorage._FileStorage__objects, {})
        obj = class_name()
        storage.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        storage.save()
        storage.reload()
        self.assertEqual(obj.to_dict(), storage.all()[key].to_dict())

    def test_reload_base(self):
        """ test the save method with BaseModel"""
        self.prepare_reload_test(BaseModel)

    def test_reload_user(self):
        """ test the save method with BaseModel"""
        self.prepare_reload_test(User)

    def test_reload_place(self):
        """ test the save method with BaseModel"""
        self.prepare_reload_test(Place)

    def test_reload_state(self):
        """ test the save method with BaseModel"""
        self.prepare_reload_test(State)

    def test_reload_amenity(self):
        """ test the save method with BaseModel"""
        self.prepare_reload_test(Amenity)

    def test_reload_city(self):
        """ test the save method with BaseModel"""
        self.prepare_reload_test(City)

    def test_reload_review(self):
        """ test the save method with BaseModel"""
        self.prepare_reload_test(Review)
