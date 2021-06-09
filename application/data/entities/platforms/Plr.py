#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
from sqlalchemy import Column, Integer, VARCHAR

from application.data.entities.AbstractEntity import AbstractEntity


class Plr(AbstractEntity):
    """
    @Entity
    This is the entity class responsible for region-level platform data management.
    The tablename is "plr"
    """

    def todict(self):
        return {
            'id': super().ide,
            'ref': self.ref,
            'name': self.name
        }

    def __init__(self, ide,
                 ref, name):
        super().__init__(ide)
        self.ref = ref
        self.name = name
