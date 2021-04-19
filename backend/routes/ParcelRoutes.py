from flask import jsonify
from werkzeug.exceptions import abort

from backend import app
from backend.data.base import session
from backend.data.entities.Parcel import Parcel



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