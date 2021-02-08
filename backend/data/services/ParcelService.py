#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad
from backend.data.entities.Parcel import Parcel
from backend.data.services.AbstractService import AbstractService

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

    """This method returns an array of all the parcels in the db"""
    def findAll(self):
        query = "SELECT * FROM parcels"
        items = self.sql.issueQueryWithResult(query)
        parcels = []
        if len(items) != 0:
            for item in items:
                parcels.append(Parcel(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8],
                                      item[9], item[10], item[11], item[12], item[13]))
        else:
            print("No parcel")
        return parcels
