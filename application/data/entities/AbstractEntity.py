#    AmazRT  -  Parcel Management System
#    First semester Technical Degree project
#      Copyright  (c) 2021 - 2022
#     - Meryem KAYA @MeryemKy
#     - Alexis LEBEL @Alestrio
#     - Malo LEGRAND @HoesMaaad
from abc import abstractmethod


class AbstractEntity:
    root_url: str
    ide: int
    editable: bool

    def __init__(self, ide):
        self.ide = ide

    @abstractmethod
    def todict(self):
        pass
