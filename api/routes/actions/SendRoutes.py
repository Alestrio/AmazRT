#    AmazRT  -  Parcel Management System
#    First semester Technical Degree project
#      Copyright  (c) 2021 - 2022
#     - Meryem KAYA @MeryemKy
#     - Alexis LEBEL @Alestrio
#     - Malo LEGRAND @HoesMaaad

from flask import jsonify, request
from werkzeug.exceptions import abort

from api import auth
from api import app
from api.data.base import session
from api.data.entities.people.Customer import Customer
from api.data.entities.people.Operator import Operator
from api.data.entities.people.Supplier import Supplier
from application.data.entities.actions.Send import Send


@app.route('/api/v1/send', methods=['POST'])
def addSend():
    req = request.get_json()
    send = Send(req['ide'], req['id_parcel'], req['id_pld'], req['id_plr'], req['send_date'], req['reception_date'],
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
