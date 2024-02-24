#!/usr/bin/python3

""" State Module for HBNB project """

import os
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Amenity Subclass of BaseModel"""

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        from models.place import place_amenity

        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity)
    else:
        name = ""
