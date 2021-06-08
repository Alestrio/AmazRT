#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
from datetime import date

from sqlalchemy import Column, ForeignKey, Date

from application.data.entities.AbstractEntity import AbstractEntity
from application.data.entities.platforms.Pld import Pld


class Pull(AbstractEntity):
    """
    @Entity
    This is the entity class responsible for the last step of the parcel pull.
    The tablename is "retirer"
    """

    def todict(self):
        return {
            'id': super().ide,
            'parcel': self.parcel,
            'pld': self.pld,
            'customer': self.customer,
            'pull_date': self.pull_date
        }

    def __init__(self, ide, parcel, pld, customer, pull_date: date):
        """Constructor"""
        super().__init__(ide)
        self.parcel = parcel
        self.pld = pld
        self.customer = customer
        self.pull_date = pull_date
