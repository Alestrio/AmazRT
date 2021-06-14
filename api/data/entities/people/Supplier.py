#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
from flask_login import UserMixin
from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from werkzeug.security import check_password_hash, generate_password_hash

from api.data.base import Base


class Supplier(Base, UserMixin):
    """
    @Entity
    This is the entity class responsible for supplier data management.
    The tablename is "fournisseur"
    """
    __tablename__ = 'fournisseur'
    id_supplier = Column('id_fournisseur', Integer, primary_key=True)
    id_city = Column('id_ville', Integer, ForeignKey('ville.id_ville'))
    ref = Column('ref_fournisseur', VARCHAR(30))
    name = Column('nom_fournisseur', VARCHAR(30))
    login = Column('login_fournisseur', VARCHAR(15))
    password = Column("mdp_fournisseur", VARCHAR(255))
    activity = Column("activite", VARCHAR(50))

    def __init__(self,
                 id_city, ref, name, login, password, activity):
        """Constructor"""
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

    def todict(self):
        return {
            'ide': self.id_supplier,
            'id_city': self.id_city,
            'ref': self.ref,
            'name': self.name,
            'login': self.login,
            'password': self.password,
            'activity': self.activity
        }
