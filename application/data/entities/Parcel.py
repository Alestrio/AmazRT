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
#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
from sqlalchemy import Column, Integer, VARCHAR

from application import Base


class Parcel(Base):
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
                 ref, ptype):
        self.ref = ref
        self.type = ptype
