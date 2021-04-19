#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad

#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
from datetime import date

from sqlalchemy import Column, ForeignKey, Date

from application import Base


class Leave(Base):
    """
    @Entity
    This is the entity class responsible for the initial deposit of the parcel.
    The tablename is "deposer"
    """
    __tablename__ = 'deposer'
    parcel = Column('id_colis', ForeignKey('colis.id_colis'), primary_key=True)
    pld = Column('id_pld', ForeignKey('pld.id_pld'), primary_key=True)
    supplier = Column('id_fournisseur', ForeignKey('fournisseur.id_fournisseur'), primary_key=True)
    deposit_date = Column('date_depot', Date)

    def __init__(self, parcel, pld, supplier, deposit_date: date):
        """Constructor"""
        self.parcel = parcel
        self.pld = pld
        self.supplier = supplier
        self.deposit_date = deposit_date

