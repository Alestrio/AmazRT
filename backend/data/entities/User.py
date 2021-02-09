#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad
from sqlalchemy import Integer, Column, String, ARRAY
from sqlalchemy.orm import relationship

from backend.data.entities.AbstractEntity import AbstractEntity
from backend.data.entities.Tracking import Tracking

"""
User

This is the data model of a user.
"""


class User(AbstractEntity):
    id = Column(Integer, primary_key=True)
    username = Column('username', String(32))
    firstname = Column('firstname', String(32))
    lastname = Column('lastname', String(32))
    email = Column('email', String(64))
    hashed_pw = Column('hashed_pw', String(255))
    address = Column('address', String(255))
    tracked_pkgs = Column('address', ARRAY(relationship("Parcel")))

    """
    Constructor:

    :Arguments:
    - serial : the database-generated id
    - username : the pseudo of the user
    - firstname : user's firstname
    - lastname : user's lastname
    - email : user's email
    - hashed_pw : user's password -> hashed and salted for security on database compromision
    - addresse : user's physical address
    - tracked_pkgs : user's tracked parcels, in the form of a array of Tracking objects. Can only be modified
      through dedicated methods.
    """

    def __init__(self, serial: int, username: str, firstname: str, lastname: str,
                 email: str, hashed_pw: str, address: str, tracked_pkgs):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.hashed_pw = hashed_pw
        self.address = address
        self.tracked_pkgs = tracked_pkgs
        super().__init__(serial)

    """This method is used on the first creation of a user, to hash the password"""

    def hashPw(self):
        pass  # TODO hash pw

    """This method is used to add a Tracking object to the array of that instance"""

    def addToTrackedPkgs(self, package: Tracking):
        pass  # TODO add to tracked
