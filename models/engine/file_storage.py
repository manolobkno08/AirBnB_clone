#!/usr/bin/python3

import json
from models.base_model import BaseModel

"""
File Storage contains code related to file
storage for the airbnb clone project
a json data format for serealizacion and
deserialization of data.
"""


class FileStorage():
    """
    this class serializes instances to
    a json file and deserializaes json
    file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    classes = {
        "BaseModel": BaseModel
    }

    def __init__(self, *args, **kwargs):
        """Constructor method"""
        pass

    def all(self):
        """
        public instance method to return
        the dictionary __object
        """
        return self.__objects

    def new(self, obj):
        """
        public instance method that sets in
        __objects with key id
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        public instance that serializes __objects
        to the json file
        """
        new_json = {}
        for key, value in self.__objects.items():
            new_json[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(new_json))

    def reload(self):
        """
        Deserialize json file __objects
        if file exists
        """
        new_dic = {}
        try:
            with open(self.__file_path, 'r') as f:
                new_dic = json.loads(f.read())
                for key, value in new_dic.items():
                    self.__objects[key] = self.classes[value["__class__"]](
                        **value)
        except:
            pass
