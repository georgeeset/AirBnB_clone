#!/usr/bin/env python3
"""
test m;odule for FileStorage class
"""
import unittest
from datetime import datetime
import time
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
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

    def test_all_1(self):
        """test the all method using BaseModel"""
        self.assertEqual(storage.all(), {})
        test_class = BaseModel()
        storage.new(test_class)
        key = "{}.{}".format(type(test_class).__name__, test_class.id)
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], test_class)

    def test_all_with_no_args(self):
        """test all method without arguments"""
        with self.assertRaises(TypeError) as e:
            FileStorage.all()
        msg = ("FileStorage.all() missing 1 required "
               "positional argument: 'self'")
        self.assertEqual(str(e.exception), msg)

    def test_new_1(self):
        """ test the new method with new BaseModel"""
        test_class = BaseModel()
        key = "{}.{}".format(type(test_class).__name__, test_class.id)
        self.assertTrue(key in FileStorage._FileStorage__objects)
        self.assertEqual(FileStorage._FileStorage__objects[key], test_class)

    def test_save_1(self):
        """ test the save method with BaseModel"""
        test_class = BaseModel()
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

    def test_reload(self):
        """ test the reload method with Base class"""
        storage.reload()
        self.assertEqual(FileStorage._FileStorage__objects, {})
        obj = BaseModel()
        storage.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        storage.save()
        storage.reload()
        self.assertEqual(obj.to_dict(), storage.all()[key].to_dict())
