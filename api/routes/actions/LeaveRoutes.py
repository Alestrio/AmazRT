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
from api.data.entities.people.Customer import Customer
from api.data.entities.actions.Leave import Leave


@app.route('/api/v1/leave', methods=['POST'])
def addLeave():
    req = request.get_json()
    leave = Leave(req['parcel'], req['pld'], req['supplier'], datetime.datetime.fromtimestamp(req['deposit_date']))
    try:
        session.add(leave)
        session.commit()
    except:
        session.rollback()
    return jsonify(201)


@app.route("/api/v1/leave", methods=['GET'])
@auth.login_required(role='operator')
def getLeaves():
    leaves = session.query(Leave).all()
    dicts = []
    for i in leaves:
        dicts.append(i.todict())
    return jsonify(dicts)


@app.route("/api/v1/leave/<int:id_leave>", methods=['GET'])
@auth.login_required(role='operator')
def getLeaveByID(id_leave: int):
    leave = session.query(Leave).filter_by(ide=id_leave).first()
    if leave is not None:
        return jsonify(leave.todict())
    abort(404)


@app.route("/api/v1/leave/<string:parcel_ref>", methods=['GET'])
def getLeaveByParcelRef(parcel_ref: str):
    parcel = session.query(Parcel).filter_by(ref=parcel_ref).first()
    leave = session.query(Leave).filter_by(parcel=parcel.id_parcel).first()
    if leave is not None:
        return jsonify(leave.todict())
    abort(404)


@app.route("/api/v1/leave/<int:id_leave>", methods=['PUT'])
@auth.login_required(role='operator')
def updateLeaveByID(id_leave: int):
    leave = session.query(Customer).filter_by(ide=id_leave).first()
    if leave is not None:
        return jsonify(leave.todict())  # TODO
    abort(404)


@app.route("/api/v1/leave/<int:id_leave>", methods=['DELETE'])
@auth.login_required(role='operator')
def deleteLeaveByID(id_leave: int):
    leave = session.query(Leave).filter_by(ide=id_leave).first()
    session.delete(leave)
    session.commit()
    abort(404)
