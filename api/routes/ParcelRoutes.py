#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
import datetime
import json

from flask import jsonify, request
from werkzeug.exceptions import abort

import api
from api import auth
from api import app
from api.data.base import session
from api.data.entities.Parcel import Parcel
from api.data.entities.actions.Leave import Leave
from api.data.entities.actions.Pull import Pull
from api.data.entities.actions.Transmit import Transmit
from application.data.data_classes.TripStage import TripStageType
from api.data.entities.actions.Send import Send


@app.route("/api/v1/parcel", methods=['GET'])
@auth.login_required(role=['operator', 'customer', 'supplier'])
def getParcels():
    data = request.args
    if not data:
        parcels = session.query(Parcel).all()
        plist = []
        for i in parcels:
            plist.append(i.todict())
        return jsonify(plist)
    else:
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
    try:
        session.add(par)
        session.commit()
    except:
        session.rollback()
    return jsonify(201)


@app.route("/api/v1/parcel/<int:id_parcel>", methods=['PUT'])
@auth.login_required(role='operator')
def updateParcelByID(id_parcel: int):
    parcel = session.query(Parcel)
    for par in parcel:
        if par.id_parcel == id_parcel:
            return jsonify(par)  # TODO
    abort(404)


def getAllPackageActions(tracking_number):
    parcel = session.query(Parcel).filter_by(ref=tracking_number).first()
    if parcel is not None:
        leave = session.query(Leave).filter_by(parcel=parcel.id_parcel).first()  # those are intended to be unique
        # that's why we are taking the first element
        pull = session.query(Pull).filter_by(parcel=parcel.id_parcel).first()
        sends = session.query(Send).filter_by(parcel=parcel.id_parcel).all()
        transmits = session.query(Transmit).filter_by(parcel=parcel.id_parcel).all()

        return {
            "parcel": parcel,
            TripStageType.LEAVE: leave,
            TripStageType.PULL: pull,
            TripStageType.SEND: sends,
            TripStageType.TRANSMIT: transmits
        }
    abort(404)


@app.route("/api/v1/parcel/update_date/<string:ref_parcel>", methods=['GET'])
def updateParcelLastDate(ref_parcel: str):
    parcel = session.query(Parcel).filter_by(ref=ref_parcel).first()
    package_all_actions = getAllPackageActions(parcel.ref)

    lastdate = datetime.datetime.fromtimestamp(0)
    last_stage = 0
    for i in package_all_actions[TripStageType.SEND]:
        if i.send_date > lastdate:
            lastdate = i.send_date
            last_stage = i
    for i in package_all_actions[TripStageType.TRANSMIT]:
        if i.send_date > lastdate:
            lastdate = i.send_date
            last_stage = i

    if isinstance(last_stage, Transmit):
        trans = session.query(Transmit).filter_by(parcel=parcel.id_parcel).first()
        trans.reception_date = datetime.datetime.now()
    else:
        send = session.query(Send).filter_by(parcel=parcel.id_parcel, pld_to_plr=last_stage.pld_to_plr).first()
        send.reception_date = datetime.datetime.now()

    try:
        session.commit()
    except:
        session.rollback()
    return jsonify(200)


@app.route("/api/v1/parcel/<int:id_parcel>", methods=['DELETE'])
@auth.login_required(role='operator')
def deleteParcelByID(id_parcel: int):
    parcel = session.query(Parcel).delete()
    for par in parcel:
        if par.id_parcel == id_parcel:
            return jsonify(par)  # TODO
    abort(404)
