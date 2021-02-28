#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad
from sqlalchemy import Column, Integer, VARCHAR

from backend.data.entities.AbstractEntity import AbstractEntity


class Parcel(AbstractEntity):
    """
    @Entity
    This is the entity class responsible for Parcel data management.
    The tablename is "colis"
    """
    __tablename__ = 'colis'
    id_parcel = Column('id_colis', Integer, primary_key=True)
    ref = Column('ref_colis', VARCHAR(30))
    type = Column('type_colis', VARCHAR(20))

    def __init__(self,
                 id_parcel, ref, ptype):
        super().__init__()
        self.id_parcel = id_parcel
        self.ref = ref
        self.type = ptype
