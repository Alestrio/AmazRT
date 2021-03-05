#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad
from datetime import date

from sqlalchemy import Column, ForeignKey, Date

from backend import Base


class Transmit(Base):
    """
    @Entity
    This is the entity class responsible for the last step of the parcel pull.
    The tablename is "retirer"
    """
    __tablename__ = 'transmetre'
    plr = Column('id_plr', ForeignKey('plr.id_plr'), primary_key=True)
    dest_plr = Column('plr_id_plr', ForeignKey('plr.id_plr'), primary_key=True)
    parcel = Column('id_colis', ForeignKey('colis.id_colis'), primary_key=True)
    send_date = Column('plr_date_envoi', Date)
    reception_date = Column('plr_date_reception', Date)

    def __init__(self, parcel, plr, dest_plr, send_date: date, reception_date: date):
        """Constructor"""
        self.parcel = parcel
        self.dest_plr = dest_plr
        self.plr = plr
        self.send_date = send_date
        self.reception_date = reception_date
