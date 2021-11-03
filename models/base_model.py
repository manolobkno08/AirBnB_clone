#!/usr/bin/python3
import uuid
import datetime

"""
Base Model Class

"""


class BaseModel():
    """Initialization"""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()

    def __str__(self):
        """String representation"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Update attribute"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Return Dictionary"""
        time = "%Y-%m-%dT%H:%M:%S.%f"

        dictionary = {}
        dictionary = self.__dict__
        dictionary['__class__'] = self.__class__.__name__

        if "created_at" in dictionary:
            dictionary["created_at"] = self.created_at.strftime(time)
        if "updated_at" in dictionary:
            dictionary["updated_at"] = self.updated_at.strftime(time)

        return dictionary
