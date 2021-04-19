#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad

from flask import jsonify
from werkzeug.exceptions import abort

from application import app
from application.data.base import session
from application.data.entities.Parcel import Parcel


@app.route("/api/v1/parcel", methods=['GET'])
def getParcels():
    parcel = session.query(Parcel).all()
    return jsonify(parcel)


@app.route("/api/v1/parcel/<int: id_par>", methods=['GET'])
def getParcelByID(id_par: int):
    parcel = session.query(Parcel).all()
    for par in parcel:
        if par.id_parcel == id_par:
            return jsonify(par)
    abort(404)


@app.route("/api/v1/parcel/<int: id_par>", methods=['PUT'])
def updateParcelByID(id_par: int):
    parcel = session.query(Parcel).update()
    for par in parcel:
        if par.id_parcel == id_par:
            return jsonify(par) #TODO
    abort(404)


@app.route("/api/v1/parcel/<int: id_par>", methods=['DELETE'])
def deleteParcelByID(id_par: int):
    parcel = session.query(Parcel).delete()
    for par in parcel:
        if par.id_parcel == id_par:
            return jsonify(par) #TODO
    abort(404)