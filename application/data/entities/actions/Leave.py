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
            'parcel': self.parcel,
            'pld': self.pld,
            'supplier': self.supplier,
            'deposit_date': self.deposit_date.timestamp()
        }

    def __init__(self, parcel=0, pld=0, supplier=0,
                 deposit_date: datetime.datetime = datetime.datetime.fromtimestamp(0)):
        """Constructor"""
        super().__init__(0)
        self.parcel = parcel
        self.pld = pld
        self.supplier = supplier
        self.deposit_date = deposit_date

    @staticmethod
    def fromdict(origin_dict):
        if origin_dict is not None:
            leavelist = []
            if not isinstance(origin_dict, dict):
                for i in origin_dict:
                    leavelist.append(Leave(i['parcel'], i['pld'], i['supplier'],
                                           datetime.datetime.fromtimestamp(i['deposit_date'])))
                return leavelist
            else:
                return Leave(origin_dict['parcel'], origin_dict['pld'], origin_dict['supplier'],
                             datetime.datetime.fromtimestamp(origin_dict['deposit_date']))
