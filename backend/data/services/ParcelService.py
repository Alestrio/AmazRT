#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad
from backend.data.services.AbstractService import AbstractService

# from backend.data.entities.Parcel import Parcel
"""
ParcelService :
Superclass : AbstractService

This is the interface to SQLService managing parcel informations
"""


class ParcelService(AbstractService):

    """Constructor"""
    def __init__(self):
        super().__init__()

    """This is the method intended to update a parcel based on an id."""
    def updateBySerial(self, serial: int, o):
        pass  # TODO update by serial

    """This is the method intended to return a parcel based on an id."""
    def getBySerial(self, serial: int):
        pass  # TODO getBySerial
