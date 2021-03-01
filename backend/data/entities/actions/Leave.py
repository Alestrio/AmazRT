#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad

#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
from datetime import date

from apt_pkg import DATE
from sqlalchemy import Column
from sqlalchemy.orm import relationship

from backend import Base


class Leave(Base):
    """
    @Entity
    This is the entity class responsible for the initial deposit of the parcel.
    The tablename is "deposer"
    """
    __tablename__ = 'deposer'
    parcel = relationship('colis', foreign_keys='colis.id_colis', primary_key=True)
    pld = relationship('pld', foreign_keys='pld.id_pld', primary_key=True)
    provider = relationship('fournisseur', foreign_keys='fournisseur.id_fournisseur', primary_key=True)
    deposit_date = Column('date_depot', DATE)

    def __init__(self, parcel: str, provider: str, deposit_date: date):
        """Constructor"""
        super().__init__()
        self.parcel = parcel
        self.provider = provider
        self.deposit_date = deposit_date

