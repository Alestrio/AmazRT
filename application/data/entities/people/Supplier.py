#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
from flask_login import UserMixin
from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from werkzeug.security import check_password_hash, generate_password_hash

from application.data.entities.AbstractEntity import AbstractEntity


class Supplier(AbstractEntity, UserMixin):
    """
    @Entity
    This is the entity class responsible for supplier data management.
    The tablename is "fournisseur"
    """
    root_url = 'supplier/'

    def todict(self):
        return {
            'id': self.ide,
            'id_city': self.id_city,
            'ref': self.ref,
            'name': self.name,
            'login': self.login,
            'password': self.password,
            'activity': self.activity
        }

    def __init__(self, ide=0, id_city=0, ref='', name='', login='', password='', activity=''):
        """Constructor"""
        super().__init__(ide)
        self.id_city = id_city
        self.ref = ref
        self.name = name
        self.login = login
        self.password = password
        self.activity = activity

    def hash_password(self):
        self.password = generate_password_hash(self.password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_id(self):
        return self.login

    @staticmethod
    def fromdict(origin_dict):
        if origin_dict:
            return Supplier(origin_dict['ide'], origin_dict['id_city'], origin_dict['ref'], origin_dict['name'],
                            origin_dict['login'], origin_dict['password'], origin_dict['activity'])

    @staticmethod
    def filter_by(param, **kwargs):
        pass  # TODO
