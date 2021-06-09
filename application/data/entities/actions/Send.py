#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
import datetime
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
    root_url = 'send/'

    def todict(self):
        return {
            'parcel': self.parcel,
            'pld': self.pld,
            'plr': self.plr,
            'send_date': self.send_date.timestamp(),
            'reception_date': self.reception_date.timestamp(),
            'pld_to_plr': self.pld_to_plr
        }

    def __init__(self, parcel=0, pld=0, plr=0, send_date: datetime.datetime = datetime.datetime.fromtimestamp(0),
                 reception_date: datetime.datetime = datetime.datetime.fromtimestamp(0), pld_to_plr: bool = False):
        """Constructor"""
        super().__init__(0)
        self.parcel = parcel
        self.pld = pld
        self.plr = plr
        self.send_date = send_date
        self.reception_date = reception_date
        self.pld_to_plr = pld_to_plr

    @staticmethod
    def fromdict(origin_dict):
        if origin_dict is not None:
            sendlist = []
            if not isinstance(origin_dict, dict):
                for i in origin_dict:
                    sendlist.append(Send(i['parcel'], i['pld'], i['plr'],
                                         datetime.datetime.fromtimestamp(i['send_date']),
                                         datetime.datetime.fromtimestamp(i['reception_date']),
                                         i['pld_to_plr']))
                return sendlist
            else:
                return Send(origin_dict['parcel'], origin_dict['pld'], origin_dict['plr'],
                            datetime.datetime.fromtimestamp(origin_dict['send_date']),
                            datetime.datetime.fromtimestamp(origin_dict['reception_date']),
                            origin_dict['pld_to_plr'])
