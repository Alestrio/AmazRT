#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
from datetime import date

from sqlalchemy import Column, ForeignKey, Date

from application.data.base import Base
from application.data.entities.platforms.Pld import Pld



class Pull(Base):
    """
    @Entity
    This is the entity class responsible for the last step of the parcel pull.
    The tablename is "retirer"
    """
    __tablename__ = 'retirer'
    parcel = Column('id_colis', ForeignKey('colis.id_colis'), primary_key=True)
    pld = Column('id_pld', ForeignKey('pld.id_pld'), primary_key=True)
    customer = Column('id_client', ForeignKey('client.id_client'), primary_key=True)
    pull_date = Column('date_retrait', Date)

    def __init__(self, parcel, pld, customer, pull_date: date):
        """Constructor"""
        self.parcel = parcel
        self.pld = pld
        self.customer = customer
        self.pull_date = pull_date
