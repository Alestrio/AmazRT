#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
from sqlalchemy import Column, Integer, VARCHAR, CHAR, Numeric, ForeignKey

from application.data.entities.AbstractEntity import AbstractEntity


class City(AbstractEntity):
    """
    @Entity
    This is the entity class responsible for cities data management.
    The tablename is "ville"
    """

    def todict(self):
        return {
            'id': super().ide,
            'id_pld': self.id_pld,
            'id_city': self.id_city,
            'name': self.name,
            'insee_code': self.insee_code,
            'postalcode': self.postalcode,
            'gps_lat': self.gps_lat,
            'gps_long': self.gps_long
        }

    def __init__(self, ide=0,
                 id_city=0, id_pld=0, name='', postalcode=0, insee_code=0, gps_lat=0, gps_long=0):
        super().__init__(ide)
        self.id_pld = id_pld
        self.id_city = id_city
        self.name = name
        self.insee_code = insee_code
        self.postalcode = postalcode
        self.gps_lat = gps_lat
        self.gps_long = gps_long

    @staticmethod
    def filter_by(cities, **kwargs):
        filters = kwargs
        filtered = []
        for city in cities:
            fil_pass = []
            for fil in filters:
                fil_pass = []
                if city[fil] == filters[fil]:
                    fil_pass.append(True)
                else:
                    fil_pass.append(False)
            if False not in fil_pass:
                filtered.append(city)
        return filtered

    @staticmethod
    def fromdict(cities):
        cities = []
        if cities is list:
            for cit in cities:
                cities.append(City(
                    cit['id'], cit['id_city'], cit['id_pld'], cit['name'], cit['postalcode'], cit['insee_code'],
                    cit['gps_lat'], cit['gps_long']
                ))
        else:
            cities = City(
                cities['id'], cities['id_city'], cities['id_pld'], cities['name'], cities['postalcode'],
                cities['insee_code'], cities['gps_lat'], cities['gps_long']
            )
