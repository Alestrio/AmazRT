#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad

"""
AbstractEntities

This is the superclass of the entities.
The entities are the data models storing user, tracking or parcel information.
It is named AbstractEntity to quickly show that it's the superclass, though the class in itself isn't declared abstract
"""


class AbstractEntity:

    def __init__(self, serial: int):
        self.serial = serial
