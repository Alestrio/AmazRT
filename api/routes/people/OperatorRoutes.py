#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad

from flask import jsonify, request
from werkzeug.exceptions import abort

from application import app
from application.data.base import session
from application.data.entities.people.Operator import Operator


@app.route("/api/v1/operator", methods=['GET'])
def getOperators():
    operators = session.query(Operator).all()  # Récuperer tous les opérateurs
    return jsonify(operators)


@app.route("/api/v1/operator/<int: id_op>", methods=['GET'])
def getOperatorByID(id_op: int):
    operator = session.query(Operator).filter_by(id_operator=id_op).first()
    if operator is not None:
        return jsonify(operator)
    abort(404)


@app.route("/api/v1/operator/<int: id_op>", methods=['PUT'])
def updateOperatorByID(id_op: int):
    operator = session.query(Operator).filter_by(id_operator=id_op).first()
    if operator is not None:
        return jsonify(operator)
    abort(404)


@app.route("/api/v1/operator/<int: id_op>", methods=['DELETE'])
def deleteOperatorByID(id_op: int):
    operator = session.query(Operator).filter_by(id_operator=id_op).first()
    new_data = request.get_json()
    if operator is not None:
        session.query(Operator).delete()
        operator.id_pld = new_data['id_pld']
        operator.lastname = new_data['lastname']
        operator.firstname = new_data['firstname']
        operator.login = new_data['login']
        operator.password = new_data['password']
        session.query(Operator).add()
    abort(404)
