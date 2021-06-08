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
from application.data.entities.platforms.Pld import Pld  # this is needed in order to use the associated foreign key

Pld(1, 1, 1, 'dummy', 'dummy')  # This is needed because PyCharm tries to delete the import (╯°□°）╯︵ ┻━┻


def hash_password(password):
    return generate_password_hash(password)


class Operator(AbstractEntity, UserMixin):
    """
    @Entity
    This is the entity class responsible for operator data management.
    The tablename is "personnel"
    """
    root_url = 'operator/'

    def todict(self):
        return {
            'id': super().ide,
            'id_pld': self.id_pld,
            'lastname': self.lastname,
            'firstname': self.firstname,
            'login': self.login,
            'password': self.password,
            'ref': self.ref
        }

    def __init__(self, ide=0, id_pld=0, lastname='', firstname='', login='', password='', ref=''):
        super().__init__(ide)
        self.id_pld = int(id_pld)
        self.lastname = lastname
        self.firstname = firstname
        self.login = login
        self.password = password
        self.ref = ref

    def hash_password(self):
        self.password = generate_password_hash(self.password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_id(self):
        return self.login

    @staticmethod
    def fromdict(param):
        pass  # TODO

    @staticmethod
    def filter_by(operator, login):
        pass  # TODO
