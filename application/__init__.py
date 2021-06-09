#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
from flask import Flask

from application.data.ApiService import ApiService

app = Flask(__name__)

service = ApiService()

from application.routes.frontend import index, products_services, tracking_expedition, common_routes, parcel_routes,\
     operator_routes, error_routes
