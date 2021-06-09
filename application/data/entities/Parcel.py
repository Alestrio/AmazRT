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
    root_url = 'parcel/'

    def todict(self):
        return {
            'ide': self.ide,
            'ref': self.ref,
            'type': self.type,
            'id_supplier': self.id_supplier,
            'id_customer': self.id_customer
        }

    def __init__(self, ide=0, ref='', ptype='', id_customer=None, id_supplier=None):
        super().__init__(ide)
        self.ide = ide
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
    def fromdict(origin_dict):
        if origin_dict is not None:
            custlist = []
            if not isinstance(origin_dict, dict):
                for i in origin_dict:
                    print(i)
                    custlist.append(Parcel(i['ide'], i['ref'], i['type'], i['id_customer'],
                                    i['id_supplier']))
                return custlist
            else:
                return Parcel(origin_dict['ide'], origin_dict['ref'], origin_dict['type'],
                              origin_dict['id_customer'], origin_dict['id_supplier'])

