#!/usr/bin/python3
import uuid
import datetime
import models

"""
Base Model Class for all models will contain id
created_at and updated
"""


class BaseModel():
    """
    Initialization of class BaseModel
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor method
        """

        if kwargs:
            kwargs["created_at"] = datetime.datetime.strptime(
                kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.datetime.strptime(
                kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")

            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        method return String representation
        """
        return ("[{}] ({}) {}".format(str(type(self).__name__),
                                      self.id, str(self.__dict__)))

    def save(self):
        """
        method to Update attrb updated_at
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        method to return a dict containing all
        key/value of__dict__
        """

        dictionary = {}
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__

        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()

        return dictionary
