#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad
from backend.data.services.AbstractService import AbstractService

"""
TrackingService :
Superclass : AbstractService

This is the interface to SQLService managing tracking informations
"""


class TrackingService(AbstractService):

    """Constructor"""
    def __init__(self):
        super().__init__()

    """This is the method intended to get tracking information based on an id."""
    def getBySerial(self, serial: int):
        pass  # TODO get by serial

    """This is the method intended to update tracking information based on an id."""
    def updateBySerial(self, serial: int, o):
        pass  # TODO update by serial
