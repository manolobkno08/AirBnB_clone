#!/usr/bin/python3

import json
from models.base_model import BaseModel

"""
File Storage Class

"""


class FileStorage():
    """Initialization"""
    __file_path = 'file.json'
    __objects = {}

    classes = {
        "BaseModel": BaseModel
    }

    def __init__(self, *args, **kwargs):
        """Constructor method"""
        pass

    def all(self):
        """Return Dictionary"""
        return self.__objects

    def new(self, obj):
        """Set <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes object"""
        new_json = {}
        for key, value in self.__objects.items():
            new_json[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(new_json))

    def reload(self):
        """Deserialize object"""
        new_dic = {}
        try:
            with open(self.__file_path, 'r') as f:
                new_dic = json.loads(f.read())
                for key, value in new_dic.items():
                    self.__objects[key] = self.classes[value["__class__"]](
                        **value)
        except:
            pass
