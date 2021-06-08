#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad

from flask import jsonify, request
from werkzeug.exceptions import abort

from api import auth
from api import app
from api.data.base import session
from api.data.entities.people.Operator import Operator


@app.route("/api/v1/operator", methods=['GET'])
@auth.login_required('operator')
def getOperators():
    operators = session.query(Operator).all()  # Récuperer tous les opérateurs
    return jsonify(operators)


@app.route("/api/v1/operator/<int: id_op>", methods=['GET'])
@auth.login_required('operator')
def getOperatorByID(id_op: int):
    operator = session.query(Operator).filter_by(id_operator=id_op).first()
    if operator is not None:
        return jsonify(operator)
    abort(404)


@app.route("/api/v1/operator/<int: id_op>", methods=['PUT'])
@auth.login_required('operator')
def updateOperatorByID(id_op: int):
    operator = session.query(Operator).filter_by(id_operator=id_op).first()
    if operator is not None:
        return jsonify(operator)
    abort(404)


@app.route("/api/v1/operator/<int: id_op>", methods=['DELETE'])
@auth.login_required('operator')
def deleteOperatorByID(id_op: int):
    operator = session.query(Operator).filter_by(id_operator=id_op).first()
    session.delete(operator)
    abort(404)
