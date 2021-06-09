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
from api.data.entities.people.Customer import Customer
from api.data.entities.people.Operator import Operator
from api.data.entities.people.Supplier import Supplier


@app.route('/api/v1/customer', methods=['POST'])
def addCustomer():
    req = request.get_json()
    cust = Customer(req['id_city'], req['ref'], req['lastname'], req['firstname'], req['login'], req['password'])
    cust.hash_password()
    session.add(cust)
    session.commit()
    return jsonify(201)


@app.route("/api/v1/customer", methods=['GET'])
@auth.login_required(role='operator')
def getCustomers():
    customers = session.query(Customer).all()
    dicts = []
    for i in customers:
        dicts.append(i.todict())
    return jsonify(dicts)


@app.route("/api/v1/customer/<int:id_cli>", methods=['GET'])
@auth.login_required(role='operator')
def getCustomerByID(id_cli: int):
    customer = session.query(Customer).filter_by(id_client=id_cli).first()
    if customer is not None:
        return jsonify(customer.todict())
    abort(404)


@app.route("/api/v1/customer/<string:login_cli>", methods=['GET'])
@auth.login_required(role=['customer', 'operator'])
def getCustomerByLOGIN(login_cli: str):
    customer = session.query(Customer).filter_by(login=login_cli).first()
    if customer is not None:
        return jsonify(customer.todict())
    abort(404)


@app.route("/api/v1/customer/<int:id_cli>", methods=['PUT'])
@auth.login_required(role='operator')
def updateCustomerByID(id_cli: int):
    customer = session.query(Customer).filter_by(id_client=id_cli).first()
    if customer is not None:
        return jsonify(customer)  # TODO
    abort(404)


@app.route("/api/v1/customer/<int:id_cli>", methods=['DELETE'])
@auth.login_required(role='operator')
def deleteCustomerByID(id_cli: int):
    customer = session.query(Customer).filter_by(id_client=id_cli).first()
    session.delete(customer)
    abort(404)


@app.route('/api/v1/login/<string:login>')
def checkIfLoginExists(login: str):
    user = {
        'as_customer': session.query(Customer).filter_by(login=login).first(),
        'as_operator': session.query(Operator).filter_by(login=login).first(),
        'as_supplier': session.query(Supplier).filter_by(login=login).first()
    }
    for i in user:
        if user[i] is not None:
            return jsonify(True)
    return jsonify(False)
