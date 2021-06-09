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
from api.data.entities.Parcel import Parcel
from api.data.entities.actions.Pull import Pull


@app.route('/api/v1/pull', methods=['POST'])
def addPull():
    req = request.get_json()
    pull = Pull(req['ide'], req['id_parcel'], req['id_pld'], req['customer'], req['pull_date'])
    session.add(pull)
    session.commit()
    return jsonify(201)


@app.route("/api/v1/pull", methods=['GET'])
@auth.login_required(role='operator')
def getPulls():
    pulls = session.query(Pull).all()
    dicts = []
    for i in pulls:
        dicts.append(i.todict())
    return jsonify(dicts)


@app.route("/api/v1/pull/<int:id_Pull>", methods=['GET'])
@auth.login_required(role='operator')
def getPullByID(id_pull: int):
    pull = session.query(Pull).filter_by(ide=id_pull).first()
    if Pull is not None:
        return jsonify(pull.todict())
    abort(404)


@app.route("/api/v1/pull/<string:parcel_ref>", methods=['GET'])
def getPullByParcelRef(parcel_ref: str):
    parcel = session.query(Parcel).filter_by(ref=parcel_ref).first()
    pull = session.query(Pull).filter_by(parcel=parcel.id_parcel).first()
    if pull is not None:
        return jsonify(pull.todict())
    abort(404)


@app.route("/api/v1/pull/<int:id_pull>", methods=['PUT'])
@auth.login_required(role='operator')
def updatePullByID(id_pull: int):
    pull = session.query(Customer).filter_by(ide=id_pull).first()
    if pull is not None:
        return jsonify(pull.todict())  # TODO
    abort(404)


@app.route("/api/v1/pull/<int:id_pull>", methods=['DELETE'])
@auth.login_required(role='operator')
def deletePullByID(id_pull: int):
    pull = session.query(Pull).filter_by(ide=id_pull).first()
    session.delete(pull)
    session.commit()
    abort(404)
