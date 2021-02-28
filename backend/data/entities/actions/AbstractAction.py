#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad
from sqlalchemy.orm import relationship

from backend.data.entities.AbstractEntity import AbstractEntity


class AbstractAction(AbstractEntity):
    """
    This is the superclass of all the actions that can be made to a Parcel
    """
    parcel = relationship('colis', foreign_keys='colis.id_colis', primary_key=True)

    def __init__(self):
        super().__init__()
