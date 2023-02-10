#!/usr/bin/python3
"""Model module Amenity.
Contains the Amenity class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class defines an Amenity.
    Attributes:
        name (str): the amenity's name.
    """

    name = ""
