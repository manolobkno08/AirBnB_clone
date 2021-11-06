#!/usr/bin/python3

from models.base_model import BaseModel

"""
User Class

"""


class User(BaseModel):
    """Initialization"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Constructor method"""
