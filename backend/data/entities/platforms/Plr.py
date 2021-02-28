#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad
from sqlalchemy import Column, Integer, VARCHAR

from backend.data.entities.AbstractEntity import AbstractEntity


class Plr(AbstractEntity):
    """
    @Entity
    This is the entity class responsible for region-level platform data management.
    The tablename is "plr"
    """
    __tablename__ = 'plr'
    id_plr = Column('id_plr', Integer, primary_key=True)
    ref = Column('ref_plr', VARCHAR(6))
    name = Column('nom_plr', VARCHAR(50))

    def __init__(self,
                 id_pld, id_plr, ref, name):
        super().__init__()
        self.id_plr = id_plr
        self.ref = ref
        self.name = name
