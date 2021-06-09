#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
from sqlalchemy import Column, Integer, VARCHAR, ForeignKey

from application.data.entities.AbstractEntity import AbstractEntity
from application.data.entities.platforms.Plr import Plr


class Pld(AbstractEntity):
    """
    @Entity
    This is the entity class responsible for department-level platform data management.
    The tablename is "pld"
    """
    def __init__(self, ide,
                 id_pld, id_plr, ref, name):
        super().__init__(ide)
        self.id_pld = id_pld
        self.id_plr = id_plr
        self.ref = ref
        self.name = name

    def todict(self):
        return {
            'id_pld': self.id_pld,
            'id_plr': self.id_plr,
            'ref': self.ref,
            'name': self.name
        }