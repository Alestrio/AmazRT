#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
import datetime
from datetime import date

from sqlalchemy import Column, ForeignKey, Date

from api.data.base import Base
from api.data.entities.platforms.Plr import Plr


class Transmit(Base):
    """
    @Entity
    This is the entity class responsible parcel transmission between two PLRs
    The tablename is "transmettre"
    """
    __tablename__ = 'transmetre'
    plr = Column('id_plr', ForeignKey('plr.id_plr'), primary_key=True)
    dest_plr = Column('plr_id_plr', ForeignKey('plr.id_plr'), primary_key=True)
    parcel = Column('id_colis', ForeignKey('colis.id_colis'), primary_key=True)
    send_date = Column('plr_date_envoi', Date)
    reception_date = Column('plr_date_reception', Date)

    def __init__(self, parcel, plr, dest_plr, send_date: datetime.datetime, reception_date: datetime.datetime):
        """Constructor"""
        self.parcel = parcel
        self.dest_plr = dest_plr
        self.plr = plr
        self.send_date = send_date
        self.reception_date = reception_date

    def todict(self):
        return {
            'parcel': self.parcel,
            'dest_plr': self.dest_plr,
            'plr': self.plr,
            'send_date': self.send_date.timestamp(),
            'reception_date': self.reception_date.timestamp()
        }
