#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
from sqlalchemy import Column, Integer, VARCHAR, CHAR, Numeric, ForeignKey, Float

from api.data.base import Base


class City(Base):
    """
    @Entity
    This is the entity class responsible for cities data management.
    The tablename is "ville"
    """
    __tablename__ = 'ville'
    id_city = Column('id_ville', Integer, primary_key=True)
    id_pld = Column('id_pld', Integer, ForeignKey('pld.id_pld'))
    name = Column('nom_ville', VARCHAR(50))
    postalcode = Column('cp', CHAR(5))
    insee_code = Column('insee_code', VARCHAR(5))
    gps_lat = Column('gps_lat', Float)
    gps_long = Column('gps_lng', Float)

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

    def todict(self):
        return {
            'ide': self.id_city,
            'id_pld': self.id_pld,
            'name': self.name,
            'insee_code': self.insee_code,
            'postalcode': self.postalcode,
            'gps_lat': self.gps_lat,
            'gps_long': self.gps_long
        }