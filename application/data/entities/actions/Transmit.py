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
from application.data.entities.platforms.Plr import Plr


class Transmit(AbstractEntity):
    """
    @Entity
    This is the entity class responsible parcel transmission between two PLRs
    The tablename is "transmettre"
    """
    root_url = 'transmit/'

    def todict(self):
        return {
            'parcel': self.parcel,
            'dest_plr': self.dest_plr,
            'plr': self.plr,
            'send_date': self.send_date.timestamp(),
            'reception_date': self.reception_date.timestamp()
        }

    def __init__(self, parcel=0, plr=0, dest_plr=0,
                 send_date: datetime.datetime = datetime.datetime.fromtimestamp(0),
                 reception_date: datetime.datetime = datetime.datetime.fromtimestamp(0)):
        """Constructor"""
        super().__init__(0)
        self.parcel = parcel
        self.dest_plr = dest_plr
        self.plr = plr
        self.send_date = send_date
        self.reception_date = reception_date

    @staticmethod
    def fromdict(origin_dict):
        if origin_dict is not None:
            transmitlist = []
            if not isinstance(origin_dict, dict):
                for i in origin_dict:
                    transmitlist.append(Transmit(i['parcel'], i['dest_plr'], i['plr'],
                                        datetime.datetime.fromtimestamp(i['send_date']),
                                        datetime.datetime.fromtimestamp(i['reception_date'])))
                return transmitlist
            else:
                return Transmit(origin_dict['parcel'], origin_dict['dest_plr'],
                                origin_dict['plr'],
                                datetime.datetime.fromtimestamp(origin_dict['send_date']),
                                datetime.datetime.fromtimestamp(origin_dict['reception_date']))
