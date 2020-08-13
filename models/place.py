#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
from models.review import Review
import models
from models.amenity import Amenity


place_amenity = Table("place_amenity", Base.metadata,
                      Column('place_id', String(60), ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="all, delete")
    amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """
            return list of review objs
            """
            rev_list = []
            for c in list(models.storage.all(Review).values()):
                if c.place_id == self.id:
                    rev_list.append(c)
            return rev_list

        @property
        def amenities(self):
            """
            return list of amenities objs
            """
            ame_list = []
            for c in list(models.storage.all(Amenity).values()):
                if c.Amenity_id == self.id:
                    ame_list.append(c)
            return ame_list

        @amenities.setter
        def amenities(self, x):
            """
            append x.id in amenity_ids
            """
            if type(x) == Amenity:
                self.amenity_ids.append(x.id)
