#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    class Amenity(BaseModel, Base):
        """amenity class"""
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        #place_amenities = relationship(
        #        "Place",
        #        secondary="place_amenity",
        #        back_populates="amenities"
        #        )
else:
    class Amenity(BaseModel):
        """amenity classs"""
        name = ""
