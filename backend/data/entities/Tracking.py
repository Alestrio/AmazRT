#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad
from sqlalchemy import Column, Integer, ARRAY, String, Date
from sqlalchemy.orm import relationship

from backend.data.entities.AbstractEntity import AbstractEntity

"""
Tracking

This is the data model used for Parcel tracking
"""


class Tracking(AbstractEntity):
    __tablename__ = 'tracking'
    id = Column(Integer, primary_key=True)
    parcel = relationship("Parcel")
    successive_positions = Column('successive_positions', ARRAY(String(32)))
    successive_date = Column('successive_dates', ARRAY(Date))

    """
    Constructor

    :Arguments:
    - serial : database-generated id
    - tracking_number : same as reference for parcel -> parcel reference
    - successive_positions : an array of string containing the PLD the parcel tripped to and from
    - successive_dates : an array of strings containing the date the parcel moved to another position
    """
    def __init__(self, serial: int, parcel, successive_positions, successive_dates):
        self.parcel = parcel
        self.successive_positions = successive_positions
        self.successive_dates = successive_dates
        super().__init__(serial)

    """This is the method adding a positions to the tracking successive positions"""
    def addToPositions(self, position: str, date):
        pass  # TODO add to positions
