#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
from sqlalchemy import Column, Integer, VARCHAR, ForeignKey

from api.data.base import Base
from api.data.entities.platforms.Plr import Plr


class Pld(Base):
    """
    @Entity
    This is the entity class responsible for department-level platform data management.
    The tablename is "pld"
    """
    __tablename__ = 'pld'
    id_pld = Column('id_pld', Integer, primary_key=True)
    id_plr = Column('id_plr', ForeignKey('plr.id_plr'))
    ref = Column('ref_pld', VARCHAR(6))
    name = Column('nom_pld', VARCHAR(50))

    def __init__(self,
                 id_pld, id_plr, ref, name):
        super().__init__()
        self.id_pld = id_pld
        self.id_plr = id_plr
        self.ref = ref
        self.name = name
