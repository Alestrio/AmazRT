#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad

#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
from flask import jsonify
from werkzeug.exceptions import abort

from api import auth
from api import app
from api.data.base import session
from api.data.entities.Parcel import Parcel


@app.route("/api/v1/parcel", methods=['GET'])
@auth.login_required('operator')
def getParcels():
    parcel = session.query(Parcel).all()
    return jsonify(parcel)


@app.route("/api/v1/parcel/<int: id_parcel>", methods=['GET'])
@auth.login_required(['operator', 'supplier', 'customer'])
def getParcelByID(id_parcel: int):
    parcel = session.query(Parcel).all()
    for par in parcel:
        if par.id_parcel == id_parcel:
            return jsonify(par)
    abort(404)


@app.route("/api/v1/parcel/<int: id_parcel>", methods=['PUT'])
@auth.login_required('operator')
def updateParcelByID(id_parcel: int):
    parcel = session.query(Parcel).update()
    for par in parcel:
        if par.id_parcel == id_parcel:
            return jsonify(par)  # TODO
    abort(404)


@app.route("/api/v1/parcel/<int: id_parcel>", methods=['DELETE'])
@auth.login_required('operator')
def deleteParcelByID(id_parcel: int):
    parcel = session.query(Parcel).delete()
    for par in parcel:
        if par.id_parcel == id_parcel:
            return jsonify(par)  # TODO
    abort(404)