#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
import datetime
from datetime import date

from sqlalchemy import Column, ForeignKey, Date, DateTime

from application.data.entities.AbstractEntity import AbstractEntity
from application.data.entities.platforms.Pld import Pld


class Leave(AbstractEntity):
    """
    @Entity
    This is the entity class responsible for the initial deposit of the parcel.
    The tablename is "deposer"
    """
    root_url = 'leave/'

    def todict(self):
        return {
            'ide': self.ide,
            'parcel': self.parcel,
            'pld': self.pld,
            'supplier': self.supplier,
            'deposit_date': self.deposit_date
        }

    def __init__(self, ide, parcel, pld, supplier, deposit_date: datetime.datetime):
        """Constructor"""
        super().__init__(ide)
        self.ide = ide
        self.parcel = parcel
        self.pld = pld
        self.supplier = supplier
        self.deposit_date = deposit_date.timestamp()

