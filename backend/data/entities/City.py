#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad
from sqlalchemy import Column, Integer, VARCHAR, CHAR, Numeric
from sqlalchemy.orm import relationship

from backend import Base


class City(Base):
    """
    @Entity
    This is the entity class responsible for cities data management.
    The tablename is "ville"
    """
    __tablename__ = 'ville'
    id_city = Column('id_ville', Integer, primary_key=True)
    id_pld = relationship('pld', foreign_keys='pld.id_pld')
    name = Column('nom_ville', VARCHAR(50))
    postalcode = Column('cp', CHAR(5))
    insee_code = Column('insee_code', VARCHAR(5))
    gps_lat = Column('gps_lat', Numeric)
    gps_long = Column('gps_long', Numeric)

    def __init__(self,
                 id_city, id_pld, name, postalcode, insee_code, gps_lat, gps_long):
        super().__init__()
        self.id_pld = id_pld
        self.id_city = id_city
        self.name = name
        self.insee_code = insee_code
        self.postalcode = postalcode
        self.gps_lat = gps_lat
        self.gps_long = gps_long

