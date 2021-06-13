#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
import json

from flask import jsonify, request
from werkzeug.exceptions import abort

from api import auth
from api import app
from api.data.base import session
from api.data.entities.Parcel import Parcel


@app.route("/api/v1/parcel", methods=['GET'])
@auth.login_required(role=['operator', 'customer', 'supplier'])
def getParcels():
    if not request.data:
        parcels = session.query(Parcel).all()
        plist = []
        for i in parcels:
            plist.append(i.todict())
        return jsonify(plist)
    else:
        data = json.loads(request.data)
        if data['id_user']:
            parcels = session.query(Parcel).filter_by(id_customer=data['id_user']).all()
            plist = []
            for i in parcels:
                plist.append(i.todict())
            return jsonify(plist)
        elif data['id_supplier']:
            parcels = session.query(Parcel).filter_by(id_supplier=data['id_supplier']).all()
            plist = []
            for i in parcels:
                plist.append(i.todict())
            return jsonify(plist)
    abort(404)


@app.route("/api/v1/parcel/<int:id_parcel>", methods=['GET'])
@auth.login_required(role=['operator', 'supplier', 'customer'])
def getParcelByID(id_parcel: int):
    parcel = session.query(Parcel).filter_by(id_parcel=id_parcel).first()
    if parcel:
        return jsonify(parcel.todict())
    abort(404)


@app.route("/api/v1/parcel/<string:ref>", methods=['GET'])
def getParcelByREF(ref: str):
    parcel = session.query(Parcel).filter_by(ref=ref).first()
    if parcel:
        return jsonify(parcel.todict())
    abort(404)


@app.route('/api/v1/parcel', methods=['POST'])
def addParcel():
    req = request.get_json()
    par = Parcel(req['ref'], req['type'], req['id_customer'], req['id_supplier'])
    session.add(par)
    session.commit()
    return jsonify(201)


@app.route("/api/v1/parcel/<int:id_parcel>", methods=['PUT'])
@auth.login_required(role='operator')
def updateParcelByID(id_parcel: int):
    parcel = session.query(Parcel)
    for par in parcel:
        if par.id_parcel == id_parcel:
            return jsonify(par)  # TODO
    abort(404)


@app.route("/api/v1/parcel/<int:id_parcel>", methods=['DELETE'])
@auth.login_required(role='operator')
def deleteParcelByID(id_parcel: int):
    parcel = session.query(Parcel).delete()
    for par in parcel:
        if par.id_parcel == id_parcel:
            return jsonify(par)  # TODO
    abort(404)
