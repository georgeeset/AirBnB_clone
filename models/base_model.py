#!/usr/bin/python3
'''
Base class that defines all common attributes/methods for other classes
'''
import uuid
from datetime import datetime
import models


class BaseModel:
    '''
    Base class with its methods and attributes
    '''

    def __init__(self, *args, **kwargs):
        """__init__ method for BaseModel class
        Args:
        args (tuple): arguments
        kwargs (dict): key word arguments
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f')
                        setattr(self, key, value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format((self.__class__.__name__),
                                     self.id, self.__dict__)

    def save(self):
        '''
        updates the public instance attributes
        '''
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        '''
        returns a dictionary containing all keys/values of
        __dict__ of the instance
        '''
        adict = dict(self.__dict__)
        adict["__class__"] = self.__class__.__name__
        adict['created_at'] = self.created_at.isoformat()
        adict['updated_at'] = self.updated_at.isoformat()
        return adict
