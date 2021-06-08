#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
from sqlalchemy import Column, Integer, VARCHAR, ForeignKey

from application.data.entities.AbstractEntity import AbstractEntity


class Parcel(AbstractEntity):
    """
    @Entity
    This is the entity class responsible for Parcel data management.
    The tablename is "colis"
    """

    def todict(self):
        return {
            'id': super().ide,
            'ref': self.ref,
            'type': self.type,
            'id_supplier': self.id_supplier,
            'id_customer': self.id_customer
        }

    def __init__(self, ide=0, ref='', ptype='', id_customer=None, id_supplier=None):
        super().__init__(ide)
        self.ref = ref
        self.type = ptype
        self.id_supplier = id_supplier
        self.id_customer = id_customer

    def asDict(self):
        return {
            "ref": self.ref,
            "type": self.type
        }

    @staticmethod
    def filter_by(param, **kwargs):
        pass

    @staticmethod
    def fromdict(param):
        pass

