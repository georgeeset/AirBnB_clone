#!/usr/bin/python3
'''
class for storing instances in a file
'''
import json


class FileStorage:
    '''
    serializes instances to a JSON file
    and deserializes JSON file to instances
    Attribute:
    __file_path: string - path to the JSON file (ex: file.json)
    __objects: dictionary - empty but will store all objects by
    <class name>.id (ex: to store a BaseModel object with id=12121212,
    the key will be BaseModel.12121212)
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        returns the dictionary __objects
        '''
        return self.__objects

    def new(self, obj):
        '''
        adds the given object to the __objects dictionary

        '''
        if obj:
            self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        '''
        serialises objects to file using json format
        '''
        new_obj = {}
        for key, value in self.__objects.items():
            new_obj[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(new_obj, f)

    def reload(self):
        '''
        deserializes the JSON file to __objects (only if
        the JSON file (__file_path) exists ; otherwise, do nothing
        in the for loop:
        "obj" is a dict, __class__ contains the class name but it's a str,
        it can't be used as a str so I used eval to strip the str off
        '''
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                json_dict = json.load(f)
                for obj in json_dict.values():
                    clas = obj["__class__"]
                    new_obj = eval("{}({})".format(clas, "**obj"))
                    self.new(new_obj)
        except FileNotFoundError:
            pass
