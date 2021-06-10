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
from api.data.entities.people.Customer import Customer
from api.data.entities.people.Operator import Operator
from api.data.entities.people.Supplier import Supplier
from api.data.entities.Parcel import Parcel
from api.data.entities.actions.Send import Send


@app.route('/api/v1/send', methods=['POST'])
def addSend():
    req = request.get_json()
    send = Send(req['parcel'], req['pld'], req['plr'], datetime.datetime.fromtimestamp(req['send_date']),
                datetime.datetime.fromtimestamp(req['reception_date']),
                req['pld_to_plr'])
    session.add(send)
    session.commit()
    return jsonify(201)


@app.route("/api/v1/send", methods=['GET'])
@auth.login_required(role='operator')
def getSends():
    sends = session.query(Send).all()
    dicts = []
    for i in sends:
        dicts.append(i.todict())
    return jsonify(dicts)


@app.route("/api/v1/send/<string:parcel_ref>", methods=['GET'])
def getSendsByParcelRef(parcel_ref: str):
    parcel = session.query(Parcel).filter_by(ref=parcel_ref).first()
    sends = session.query(Send).filter_by(parcel=parcel.id_parcel)
    if sends is not None:
        sendlist = []
        for i in sends:
            sendlist.append(i.todict())
        return jsonify(sendlist)
    abort(404)


@app.route("/api/v1/send/<int:id_send>", methods=['GET'])
@auth.login_required(role='operator')
def getSendByID(id_send: int):
    send = session.query(Send).filter_by(ide=id_send).first()
    if Send is not None:
        return jsonify(send.todict())
    abort(404)


@app.route("/api/v1/send/<int:id_send>", methods=['PUT'])
@auth.login_required(role='operator')
def updateSendByID(id_send: int):
    send = session.query(Customer).filter_by(ide=id_send).first()
    if send is not None:
        return jsonify(send.todict())  # TODO
    abort(404)


@app.route("/api/v1/send/<int:id_send>", methods=['DELETE'])
@auth.login_required(role='operator')
def deleteSendByID(id_send: int):
    send = session.query(Send).filter_by(ide=id_send).first()
    session.delete(send)
    session.commit()
    abort(404)
