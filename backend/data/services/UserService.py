#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad
from backend.data.services.AbstractService import AbstractService

"""
UserService :
Superclass : AbstractService

This is the interface to SQLService managing user informations
"""


class UserService(AbstractService):

    """Constructor"""
    def __init__(self):
        super().__init__()

    """This is the method intended to get user information based on an id."""
    def getBySerial(self, serial: int):
        pass  # TODO get by serial

    """This is the method intended to update user information based on an id."""
    def updateBySerial(self, serial: int, o):
        pass  # TODO update by serial
