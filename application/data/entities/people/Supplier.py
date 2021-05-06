#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from werkzeug.security import check_password_hash, generate_password_hash

from application.data.base import Base


class Supplier(Base):
    """
    @Entity
    This is the entity class responsible for supplier data management.
    The tablename is "fournisseur"
    """
    __tablename__ = 'fournisseur'
    id_supplier = Column('id_fournisseur', Integer, primary_key=True)
    id_city = Column('id_ville', Integer, ForeignKey('ville.id_ville'))
    ref = Column('ref_fournisseur', VARCHAR(15))
    name = Column('nom_fournisseur', VARCHAR(30))
    address = Column('adresse_fournisseur', VARCHAR(100))
    login = Column('login_fournisseur', VARCHAR(15))
    password = Column("mdp_fournisseur", VARCHAR(255))

    def __init__(self,
                 id_city, ref, name, address, login, password):
        """Constructor"""
        self.id_city = id_city
        self.ref = ref
        self.name = name
        self.address = address
        self.login = login
        self.password = password

    def hash_password(self, password):
        self.password = generate_password_hash(self.password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
