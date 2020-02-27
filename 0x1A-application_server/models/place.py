#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base, Column, String
from sqlalchemy import Float, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.city import City
from models.user import User


place_amenity = Table(
        'place_amenity', Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'),
               primary_key=True, nullable=False),
        Column('amenity_id', String(60), ForeignKey('amenities.id'),
               primary_key=True, nullable=False)
        )


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey(City.id), nullable=False)
    user_id = Column(String(60), ForeignKey(User.id), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    reviews = relationship("Review", "place")

    amenities = relationship(
            "Amenity", backref="place_amenities", secondary="place_amenity",
            viewonly=False)

    @property
    def reviews(self):
        """returns a list of reviews with same place_id"""
        ret = []
        for k, v in storage.all().keys():
            if k.split(".")[0] == "Review":
                if v.place_id == self.id:
                    ret.append(v)
        return ret
