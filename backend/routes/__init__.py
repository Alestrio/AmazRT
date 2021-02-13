#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad

from backend.data.entities import *
from backend.data.base import Session, engine, Base

Base.metadata.create_all(engine)

session = Session()
