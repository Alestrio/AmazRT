#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad
from flask import jsonify

from backend import app, session
from backend.data.entities.Tracking import Tracking


@app.route("/tracking/all")
def getAllTracking():
    trackings = session.query(Tracking).all()
    return jsonify(trackings)


@app.route("/tracking/get")
def getTrackingByID():
    return ""


@app.route("/tracking/update")
def updateTrackingByID():
    return ""
