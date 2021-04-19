#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad

#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
from sqlalchemy import Column, Integer, VARCHAR, ForeignKey

from application import Base


class Operator(Base):
    """
    @Entity
    This is the entity class responsible for operator data management.
    The tablename is "personnel"
    """
    __tablename__ = 'personnel'
    id_operator = Column('id_personnel', Integer, primary_key=True)
    id_pld = Column('id_pld', Integer, ForeignKey('pld.id_pld'))
    lastname = Column('nom_personnel', VARCHAR(50))
    firstname = Column('prenom_personnel', VARCHAR(50))
    login = Column('login_personnel', VARCHAR(15))
    password = Column('mdp_personnel', VARCHAR(15))

    def __init__(self,
                 id_pld, lastname, firstname, login, password):
        self.id_pld = id_pld
        self.lastname = lastname
        self.firstname = firstname
        self.login = login
        self.password = password
