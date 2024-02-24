#!/usr/bin/python3

""" Place Module for HBNB project """

import os
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, Table, ForeignKey
from sqlalchemy.orm import relationship

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table(
            "place_amenity",
            Base.metadata,
            Column(
                "place_id",
                String(60),
                ForeignKey(
                    "places.id",
                    onupdate='CASCADE',
                    ondelete='CASCADE'),
                primary_key=True,
                nullable=False),
            Column(
                "amenity_id",
                String(60),
                ForeignKey(
                    "amenities.id",
                    onupdate='CASCADE',
                    ondelete='CASCADE'),
                primary_key=True,
                nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

        reviews = relationship(
                "Review",
                backref="place",
                cascade="all, delete, delete-orphan")

        amenities = relationship(
                "Amenity",
                secondary="place_amenity",
                viewonly=False,
                back_populates="place_amenities")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """ returns the reviews with place.id == Place.id """

            list_reviews = []
            for key, obj in models.storage.all().items():
                if "Review" in key:
                    if obj.place_id == self.id:
                        list_reviews += [obj]

            return list_reviews

        @property
        def amenities(self):
            """ Retrns the list of aAmenity instances basef on the ids """

            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """  Adds a new Amenity.id to the attribute """

            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
