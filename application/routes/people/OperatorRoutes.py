#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad

from flask import jsonify
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
    operators = session.query(Operator).all()
    for op in operators:
        if op.id_operator == id_op:
            return jsonify(op)
    abort(404)


@app.route("/api/v1/operator/<int: id_op>", methods=['PUT'])
def updateOperatorByID(id_op: int):
    operators = session.query(Operator).update()
    for op in operators:
        if op.id_operator == id_op:
            return jsonify(op) #TODO
    abort(404)


@app.route("/api/v1/operator/<int: id_op>", methods=['DELETE'])
def deleteOperatorByID(id_op: int):
    operators = session.query(Operator).delete()
    for op in operators:
        if op.id_operator == id_op:
            return jsonify(op) #TODO
    abort(404)