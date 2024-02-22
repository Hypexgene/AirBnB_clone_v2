#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Represents a user for a database.

    Inherits from SQLAlchemy Base and links to the table users.

    Attributes:
        __tablename__ (str): The name of the table to store users.
        email: The user's email address.
        password: The user's password.
        first_name: The user's first name.
        last_name: The user's last name.
        places: Relationship to the Place class. If the User object is deleted,
                all linked Place objects must be automatically deleted.
                Also, the reference from a Place object to its User is named user.
        reviews: Relationship to the Review class. If the User object is deleted,
                 all linked Review objects must be automatically deleted.
                 Also, the reference from a Review object to its User is named user.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", backref="user", cascade="all, delete")
    reviews = relationship("Review", backref="user", cascade="all, delete")
