#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad
from abc import abstractmethod

from backend.data import SQLService as sqls

"""
AbstractService

This is the superclass of the services.
The services are the interfaces between the programme, and the SQLService class.
It is names AbstractService to quickly show that it's the superclass, though nothing or almost nothing is declared
abstract.
"""


class AbstractService:
    """Constructor"""
    def __init__(self):
        self.sql = sqls.SQLService()

    """
    This is the method intended to return an entity based on an id.
    It's an abstract method, which means it needs to be redefined.
    """
    @abstractmethod
    def getBySerial(self, serial: int):
        pass

    """
    This is the method intended to update an item in the db based on an id.
    Again, it's abstract.
    """
    @abstractmethod
    def updateBySerial(self, serial: int, o):
        pass
