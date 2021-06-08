#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
from datetime import date

from sqlalchemy import ForeignKey, Column, Boolean, Date

from application.data.entities.AbstractEntity import AbstractEntity
from application.data.entities.platforms.Plr import Plr
from application.data.entities.platforms.Pld import Pld


class Send(AbstractEntity):
    """
    @Entity
    This is the entity class responsible for the middle step of the parcel trip.
    The tablename is "envoyer"
    """

    def todict(self):
        return {
            'id': super().ide,
            'parcel': self.parcel,
            'pld': self.pld,
            'plr': self.plr,
            'send_date': self.send_date,
            'reception_date': self.reception_date,
            'pld_to_plr': self.pld_to_plr
        }

    def __init__(self, ide, parcel, pld, plr, send_date: date, reception_date: date, pld_to_plr: bool):
        """Constructor"""
        super().__init__(ide)
        self.parcel = parcel
        self.pld = pld
        self.plr = plr
        self.send_date = send_date
        self.reception_date = reception_date
        self.pld_to_plr = pld_to_plr
