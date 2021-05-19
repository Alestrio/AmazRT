#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
from flask_login import UserMixin
from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash

from application.data.base import Base
from application.data.entities.platforms.Pld import Pld  # this is needed in order to use the associated foreign key

Pld(1, 1, 'dummy', 'dummy')  # This is needed because PyCharm tries to delete the import (╯°□°）╯︵ ┻━┻


def hash_password(password):
    return generate_password_hash(password)


class Operator(Base, UserMixin):
    """
    @Entity
    This is the entity class responsible for operator data management.
    The tablename is "personnel"
    """
    __tablename__ = 'personnel'
    id_operator = Column('id_personnel', Integer, primary_key=True)
    id_pld = Column('id_pld', Integer, ForeignKey('pld.id_pld'))
    ref = Column('ref_personnel', VARCHAR(100))
    lastname = Column('nom_personnel', VARCHAR(50))
    firstname = Column('prenom_personnel', VARCHAR(50))
    login = Column('login_personnel', VARCHAR(15))
    password = Column('mdp_personnel', VARCHAR(255))

    def __init__(self,
                 id_pld, lastname, firstname, login, password, ref):
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
