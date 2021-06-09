#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
from flask_login import UserMixin
from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash

from application.data.entities.AbstractEntity import AbstractEntity


class Customer(AbstractEntity, UserMixin):
    """
    @Entity
    This is the entity class responsible for customer data management.
    The tablename is "client"
    """
    root_url = 'customer/'

    def todict(self):
        return {
            'ide': self.ide,
            'id_city': self.id_city,
            'ref': self.ref,
            'lastname': self.lastname,
            'firstname': self.firstname,
            'login': self.login,
            'password': self.password
        }

    def __init__(self, ide=0, id_city=0, ref=0, lastname='', firstname='', login='', password=''):
        """Constructor"""
        super().__init__(ide)
        self.ide = ide
        self.id_city = id_city
        self.ref = ref
        self.lastname = lastname
        self.firstname = firstname
        self.login = login
        self.password = password

    def hash_password(self):
        self.password = generate_password_hash(self.password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_id(self):
        return self.login

    @staticmethod
    def fromdict(origin_dict):
        if origin_dict is not None:
            custlist = []
            if origin_dict is not dict:
                for i in origin_dict:
                    print(i)
                    custlist.append(Customer(i['ide'], i['id_city'], i['ref'], i['lastname'],
                                    i['firstname'], i['login'], i['password']))
                return custlist
            else:
                return Customer(origin_dict['ide'], origin_dict['id_city'], origin_dict['ref'], origin_dict['lastname'],
                                origin_dict['firstname'], origin_dict['login'], origin_dict['password'])

    @staticmethod
    def filter_by(customer, **kwargs):
        pass  # TODO

