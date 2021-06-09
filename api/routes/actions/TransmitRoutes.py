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
from application.data.entities.actions.Transmit import Transmit


@app.route('/api/v1/transmit', methods=['POST'])
def addTransmit():
    req = request.get_json()
    transmit = Transmit(req['ide'], req['id_parcel'], req['id_plr'], req['dest_plr'], req['send_date'],
                        req['reception_date'])
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
