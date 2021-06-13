#    AmazRT  -  Parcel Management System
#    First semester Technical Degree project
#      Copyright  (c) 2021 - 2022
#     - Meryem KAYA @MeryemKy
#     - Alexis LEBEL @Alestrio
#     - Malo LEGRAND @HoesMaaad
import json
import sys

import requests

from application.util import config

if __name__ == '__main__':
    filepath = sys.argv[0]
    if filepath:
        with open(filepath, 'r') as file:
            with json.loads(file.read()) as json_result:
                requests.get(config.api_url+'parcel/update_date/'+json_result['ref'])
