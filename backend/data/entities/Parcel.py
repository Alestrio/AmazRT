#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad
from backend.data.entities.AbstractEntity import AbstractEntity

"""
Parcel :

This is the data model of a parcel.
It contains all the informations related to the parcel in itself (not the tracking)
"""


class Parcel(AbstractEntity):

    """
    Constructor:

    :Arguments:
    - serial : database id
    - reference : parcel number, same as tracking number
    - condition : if the parcel is damaged or not
    - weight, length, width, height
    - sender : name and address of the sender
    - receiver : name and address of the receiver
    - dangerous : if the parcel contains any dangerous material
    - content : content of the parcel
    - deposit_date
    - destination_pld, current_position
    """
    def __init__(self, serial: int, reference: str, condition: str, weight: float,
                 length: float, width: float, height: float, sender: str, receiver: str,
                 dangerous: bool, content: str, deposit_date: str, destination_pld, current_position):
        super(Parcel, self).__init__(serial)
        self.reference = reference
        self.condition = condition
        self.weight = weight
        self.length = length
        self.width = width
        self.height = height
        self.sender = sender
        self.receiver = receiver
        self.dangerous = dangerous
        self.content = content
        self.deposit_date = deposit_date
        self.destination_pld = destination_pld
        self.current_position = current_position
