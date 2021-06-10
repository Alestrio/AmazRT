#    AmazRT  -  Parcel Management System
#    First semester Technical Degree project
#      Copyright  (c) 2021 - 2022
#     - Meryem KAYA @MeryemKy
#     - Alexis LEBEL @Alestrio
#     - Malo LEGRAND @HoesMaaad
import datetime

from flask import jsonify, request
from werkzeug.exceptions import abort

from api import auth
from api import app
from api.data.base import session
from api.data.entities.Parcel import Parcel
from api.data.entities.actions.Send import Send
from api.data.entities.people.Customer import Customer
from api.data.entities.people.Operator import Operator
from api.data.entities.people.Supplier import Supplier
from api.data.entities.actions.Transmit import Transmit


@app.route('/api/v1/transmit', methods=['POST'])
def addTransmit():
    req = request.get_json()
    transmit = Transmit(req['parcel'], req['plr'], req['dest_plr'], datetime.datetime.fromtimestamp(req['send_date']),
                        datetime.datetime.fromtimestamp(req['reception_date']))
    session.add(transmit)
    session.commit()
    return jsonify(201)


@app.route("/api/v1/transmit", methods=['GET'])
@auth.login_required(role='operator')
def getTransmits():
    transmits = session.query(Transmit).all()
    dicts = []
    for i in transmits:
        dicts.append(i.todict())
    return jsonify(dicts)


@app.route("/api/v1/transmit/<string:parcel_ref>", methods=['GET'])
def getTransmitsByParcelRef(parcel_ref: str):
    parcel = session.query(Parcel).filter_by(ref=parcel_ref).first()
    transmits = session.query(Transmit).filter_by(parcel=parcel.id_parcel)
    if transmits is not None:
        transmitlist = []
        for i in transmits:
            transmitlist.append(i.todict())
        return jsonify(transmitlist)
    abort(404)


@app.route("/api/v1/transmit/<int:id_transmit>", methods=['GET'])
@auth.login_required(role='operator')
def getTransmitByID(id_transmit: int):
    transmit = session.query(Transmit).filter_by(ide=id_transmit).first()
    if transmit is not None:
        return jsonify(transmit.todict())
    abort(404)


@app.route("/api/v1/transmit/<int:id_transmit>", methods=['PUT'])
@auth.login_required(role='operator')
def updateTransmitByID(id_transmit: int):
    transmit = session.query(Customer).filter_by(ide=id_transmit).first()
    if transmit is not None:
        return jsonify(transmit.todict())  # TODO
    abort(404)


@app.route("/api/v1/transmit/<int:id_transmit>", methods=['DELETE'])
@auth.login_required(role='operator')
def deleteTransmitByID(id_transmit: int):
    transmit = session.query(Transmit).filter_by(ide=id_transmit).first()
    session.delete(transmit)
    session.commit()
    abort(404)
