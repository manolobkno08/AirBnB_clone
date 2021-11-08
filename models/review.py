#!/usr/bin/python3

from models.base_model import BaseModel


"""define the review class"""


class Review(BaseModel):
    """represent a reviem"""

    place_id = ""
    user_id = ""
    text = ""
