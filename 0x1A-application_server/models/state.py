#!/usr/bin/python3
"""This is the state class for AirBnB"""
from models.base_model import BaseModel, Base, Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models
import os


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        @property
        def cities(self):
            """get the cities with state_id equal"""
            ret = []
            for k, v in models.storage.all().items():
                if k.split(".")[0] == "City":
                    if v.state_id == self.id:
                        ret.append(v)
            return ret
