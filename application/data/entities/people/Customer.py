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


class Customer(Base, UserMixin):
    """
    @Entity
    This is the entity class responsible for customer data management.
    The tablename is "client"
    """
    __tablename__ = 'client'
    id_client = Column('id_client', Integer, primary_key=True)
    id_city = Column('id_ville', Integer, ForeignKey('ville.id_ville'))
    ref = Column('ref_client', VARCHAR(15))
    lastname = Column('nom_client', VARCHAR(30))
    firstname = Column('prenom_client', VARCHAR(30))
    address = Column('adresse_client', VARCHAR(100))
    login = Column('login_client', VARCHAR(15))
    password = Column("mdp_client", VARCHAR(255))

    def __init__(self,
                 id_city, ref, lastname, firstname, address, login, password):
        """Constructor"""
        self.id_city = id_city
        self.ref = ref
        self.lastname = lastname
        self.firstname = firstname
        self.address = address
        self.login = login
        self.password = password

    def hash_password(self):
        self.password = generate_password_hash(self.password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_id(self):
        return self.login