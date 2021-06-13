#    AmazRT  -  Parcel Management System
#    First semester Technical Degree project
#      Copyright  (c) 2021 - 2022
#     - Meryem KAYA @MeryemKy
#     - Alexis LEBEL @Alestrio
#     - Malo LEGRAND @HoesMaaad
import json
import os

import pysftp as pysftp

from application.data.data_classes.TripStage import LocationType
from application.data.entities.Parcel import Parcel
from application.util import config


class JsonParcelService:

    @staticmethod
    def createParcel(parcel: Parcel):
        path = config.parcel_root_file_path
        with open(path+parcel.ref+'.json', 'w') as file:
            file.write(json.dumps(parcel.todict()))
            file.close()

    @staticmethod
    def moveParcel(parcel, dest_type: LocationType, dest_id):
        available_dests = config.available_dests
        for i in available_dests:
            if i['type'] == dest_type.value and i['id'] == int(dest_id) and parcel:
                with pysftp.Connection(i['ip'], username=config.siteusername,
                                       password=config.sitepassword) as conn:
                    conn.put(config.parcel_root_file_path+parcel.ref+'.json',
                             config.parcel_root_file_path+parcel.ref+'.json')
                    os.remove(config.parcel_root_file_path+parcel.ref+'.json')
                    break
