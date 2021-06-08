#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
from datetime import date

from sqlalchemy import Column, ForeignKey, Date

from application.data.entities.AbstractEntity import AbstractEntity
from application.data.entities.platforms.Plr import Plr


class Transmit(AbstractEntity):
    """
    @Entity
    This is the entity class responsible parcel transmission between two PLRs
    The tablename is "transmettre"
    """

    def todict(self):
        return {
            'id': super().ide,
            'parcel': self.parcel,
            'dest_plr': self.dest_plr,
            'plr': self.plr,
            'send_date': self.send_date,
            'reception_date': self.reception_date
        }

    def __init__(self, ide, parcel, plr, dest_plr, send_date: date, reception_date: date):
        """Constructor"""
        super().__init__(ide)
        self.parcel = parcel
        self.dest_plr = dest_plr
        self.plr = plr
        self.send_date = send_date
        self.reception_date = reception_date
