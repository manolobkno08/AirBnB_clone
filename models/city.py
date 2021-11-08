#!/usr/bin/python3

"""module inherits from baseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """represent a city"""

    state_id = ""
    name = ""
