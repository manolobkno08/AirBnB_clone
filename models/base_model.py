#!/usr/bin/python3
import uuid
from datetime import datetime
import models

"""
Base Model Class

"""


class BaseModel():
    """Initialization"""

    def __init__(self, *args, **kwargs):
        """Constructor method"""

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
        """String representation"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Update attribute"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return Dictionary"""

        dictionary = {}
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__

        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()

        return dictionary
