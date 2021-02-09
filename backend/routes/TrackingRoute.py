#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad

from backend import app
from backend.data.services.TrackingService import TrackingService

@app.route("/")
@app.route("/parcel/all")
def getAllParcels():
    return "jsonify(service.findAll())"