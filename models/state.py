#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import models
from os import getenv
from models.base_model import Base
from sqlalchemy import Column
from models.city import City
from sqlalchemy import String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """get a list of related city"""
            return [c for c in models.storage.all(City).values()
                    if city.state_id == self.id]
