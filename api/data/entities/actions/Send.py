#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
import datetime
from datetime import date

from sqlalchemy import ForeignKey, Column, Boolean, Date

from application.data.base import Base
from application.data.entities.platforms.Plr import Plr
from application.data.entities.platforms.Pld import Pld


class Send(Base):
    """
    @Entity
    This is the entity class responsible for the middle step of the parcel trip.
    The tablename is "envoyer"
    """
    __tablename__ = 'envoyer'
    parcel = Column('id_colis', ForeignKey('colis.id_colis'), primary_key=True)
    pld = Column('id_pld', ForeignKey('pld.id_pld'), primary_key=True)
    plr = Column('id_plr', ForeignKey('pld.id_plr'), primary_key=True)
    send_date = Column('date_envoi', Date)
    reception_date = Column('date_reception', Date)
    pld_to_plr = Column('pld_to_plr', Boolean)

    def __init__(self, parcel, pld, plr, send_date: datetime.datetime, reception_date: datetime.datetime,
                 pld_to_plr: bool):
        """Constructor"""
        self.parcel = parcel
        self.pld = pld
        self.plr = plr
        self.send_date = send_date
        self.reception_date = reception_date
        self.pld_to_plr = pld_to_plr

    def todict(self):
        return {
            'parcel': self.parcel,
            'pld': self.pld,
            'plr': self.plr,
            'send_date': self.send_date.timestamp(),
            'reception_date': self.reception_date.timestamp(),
            'pld_to_plr': self.pld_to_plr
        }
