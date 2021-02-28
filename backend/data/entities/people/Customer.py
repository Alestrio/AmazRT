#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad
from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship

from backend.data.entities.AbstractEntity import AbstractEntity


class Customer(AbstractEntity):
    """
    @Entity
    This is the entity class responsible for customer data management.
    The tablename is "client"
    """
    __tablename__ = 'client'
    id_client = Column('id_client', Integer)
    id_city = relationship('ville', foreign_keys='ville.id_ville')
    ref = Column('ref_client', VARCHAR(15))
    lastname = Column('nom_client', VARCHAR(30))
    firstname = Column('prenom_client', VARCHAR(30))
    address = Column('adresse_client', VARCHAR(100))
    login = Column('login_client', VARCHAR(15))
    password = Column("mdp_client", VARCHAR(15))

    def __init__(self,
                 id_client, id_city, ref, lastname, firstname, address, login, password):
        """Constructor"""
        super().__init__()
        self.id_client = id_client
        self.id_city = id_city
        self.ref = ref
        self.lastname = lastname
        self.firstname = firstname
        self.address = address
        self.login = login
        self.password = password

