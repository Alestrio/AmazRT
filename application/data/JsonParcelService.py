#    AmazRT  -  Parcel Management System
#    First semester Technical Degree project
#      Copyright  (c) 2021 - 2022
#     - Meryem KAYA @MeryemKy
#     - Alexis LEBEL @Alestrio
#     - Malo LEGRAND @HoesMaaad
import json
import os

import pysftp as pysftp

from application.data.entities.AbstractEntity import AbstractEntity
from application.data.entities.Parcel import Parcel
from application.util import config


class JsonParcelService:

    @staticmethod
    def createParcel(parcel: Parcel):
        path = config.parcel_root_file_path
        with open(parcel.ref+'.json', 'rw') as file:
            file.write(json.dumps(parcel.todict()))

    @staticmethod
    def moveParcel(parcel, dest_type: AbstractEntity, dest_id):
        available_dests = config.available_dests
        if (dest_type, dest_id, any) in available_dests:
            with pysftp.Connection(available_dests[2], username=available_dests[3],
                                   password=available_dests[4]) as conn :
                with conn.cd(config.parcel_root_file_path):
                    conn.put(parcel.ref+'.json', config.parcel_root_file_path+parcel.ref+'.json')
                    os.remove(config.parcel_root_file_path+parcel.ref+'.json')

