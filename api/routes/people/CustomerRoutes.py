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
from application.data.entities.people.Customer import Customer


@app.route("/api/v1/customer", methods=['GET'])
def getCustomers():
    customers = session.query(Customer).all()
    return jsonify(customers)


@app.route("/api/v1/customer/<int: id_cli>", methods=['GET'])
def getCustomerByID(id_cli: int):
    customer = session.query(Customer).filter_by(id_client=id_cli).first()
    if customer is not None:
        return jsonify(customer)
    abort(404)


@app.route("/api/v1/customer/<int: id_cli>", methods=['PUT'])
def updateCustomerByID(id_cli: int):
    customer = session.query(Customer).filter_by(id_client=id_cli).first()
    if customer is not None:
        return jsonify(customer)
    abort(404)


@app.route("/api/v1/customer/<int: id_cli>", methods=['DELETE'])
def deleteCustomerByID(id_cli: int):
    customer = session.query(Customer).filter_by(id_client=id_cli).first()
    new_data = request.get_json()
    if customer is not None:
        session.query(Customer).delete()
        customer.id_city = new_data['id_city']
        customer.ref = new_data['ref']
        customer.lastname = new_data['lastname']
        customer.firstname = new_data['firstname']
        customer.address = new_data['address']
        customer.login = new_data['login']
        customer.password = new_data['password']
        session.query(Customer).add()
    abort(404)