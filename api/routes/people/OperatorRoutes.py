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


@app.route('/api/v1/operator', methods=['POST'])
def addOperator():
    req = request.get_json()
    op = Operator(req['id_pld'], req['lastname'], req['firstname'], req['login'], req['password'], req['ref'])
    op.hash_password()
    try:
        session.add(op)
        session.commit()
    except:
        session.rollback()
    return jsonify(201)


@app.route("/api/v1/operator", methods=['GET'])
@auth.login_required(role='operator')
def getOperators():
    operators = session.query(Operator).all()  # Récuperer tous les opérateurs
    return jsonify(operators)


@app.route("/api/v1/operator/<int:id_op>", methods=['GET'])
@auth.login_required(role='operator')
def getOperatorByID(id_op: int):
    operator = session.query(Operator).filter_by(id_operator=id_op).first()
    if operator is not None:
        return jsonify(operator.todict())
    abort(404)


@app.route("/api/v1/operator/<string:login>", methods=['GET'])
@auth.login_required(role='operator')
def getOperatorByLOGIN(login: str):
    operator = session.query(Operator).filter_by(login=login).first()
    if operator is not None:
        return jsonify(operator.todict())
    abort(404)


@app.route("/api/v1/operator/<int:id_op>", methods=['PUT'])
@auth.login_required(role='operator')
def updateOperatorByID(id_op: int):
    operator = session.query(Operator).filter_by(id_operator=id_op).first()
    if operator is not None:
        return jsonify(operator)
    abort(404)


@app.route("/api/v1/operator/<int:id_op>", methods=['DELETE'])
@auth.login_required(role='operator')
def deleteOperatorByID(id_op: int):
    operator = session.query(Operator).filter_by(id_operator=id_op).first()
    session.delete(operator)
    abort(404)
