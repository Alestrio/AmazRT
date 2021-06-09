#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
import datetime
from datetime import date

from sqlalchemy import Column, ForeignKey, Date

from application.data.entities.AbstractEntity import AbstractEntity
from application.data.entities.platforms.Pld import Pld


class Pull(AbstractEntity):
    """
    @Entity
    This is the entity class responsible for the last step of the parcel pull.
    The tablename is "retirer"
    """
    root_url = 'pull/'

    def todict(self):
        return {
            'parcel': self.parcel,
            'pld': self.pld,
            'customer': self.customer,
            'pull_date': self.pull_date
        }

    def __init__(self, parcel=0, pld=0, customer=0,
                 pull_date: datetime.datetime = datetime.datetime.fromtimestamp(0)):
        """Constructor"""
        super().__init__(0)
        self.parcel = parcel
        self.pld = pld
        self.customer = customer
        self.pull_date = pull_date

    @staticmethod
    def fromdict(origin_dict):
        if origin_dict is not None:
            pulllist = []
            if not isinstance(origin_dict, dict):
                for i in origin_dict:
                    pulllist.append(Pull(i['parcel'], i['pld'], i['customer'],
                                         datetime.datetime.fromtimestamp(i['pull_date'])))
                return pulllist
            else:
                return Pull(origin_dict['parcel'], origin_dict['pld'], origin_dict['customer'],
                            datetime.datetime.fromtimestamp(origin_dict['pull_date']))
