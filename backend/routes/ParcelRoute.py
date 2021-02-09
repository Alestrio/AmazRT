#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad
from flask import jsonify

from backend import app
from backend.data.services.ParcelService import ParcelService

service = ParcelService()

@app.route("/")
@app.route("/parcel/all")
def getAllParcels():
    return "jsonify(service.findAll())"

@app.route("/parcel/get")
def getBySerial():
    return "!"

@app.route("/parcel/update")
def updateBySerial():
    return "!"

@app.route("/parcel/!")
def findAll():
    return "!"
