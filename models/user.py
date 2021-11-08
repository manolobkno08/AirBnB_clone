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
