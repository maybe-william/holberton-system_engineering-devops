#!/usr/bin/python3
"""This is the review class"""
from models.base_model import BaseModel, Base, String, Column, ForeignKey
from models.user import User
from models.place import Place


class Review(BaseModel, Base):
    """This is the class for Review
    Attributes:
        place_id: place id
        user_id: user id
        text: review description
    """
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey(Place.id), nullable=False)
    user_id = Column(String(60), ForeignKey(User.id), nullable=False)
    text = Column(String(1024), nullable=False)
