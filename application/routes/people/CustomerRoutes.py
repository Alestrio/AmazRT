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
from application.data.entities.people.Customer import Customer


@app.route("/api/v1/customer", methods=['GET'])
def getCustomers():
    customers = session.query(Customer).all()
    return jsonify(customers)


@app.route("/api/v1/customer/<int: id_cli>", methods=['GET'])
def getCustomerByID(id_cli: int):
    customers = session.query(Customer).all()
    for cli in customers:
        if cli.id_client == id_cli:
            return jsonify(cli)
    abort(404)


@app.route("/api/v1/customer/<int: id_cli>", methods=['PUT'])
def updateCustomerByID(id_cli: int):
    customers = session.query(Customer).update()
    for cli in customers:
        if cli.id_client == id_cli:
            return jsonify(cli) #TODO
    abort(404)


@app.route("/api/v1/customer/<int: id_cli>", methods=['DELETE'])
def deleteCustomerByID(id_cli: int):
    customers = session.query(Customer).delete()
    for cli in customers:
        if cli.id_client == id_cli:
            return jsonify(cli) #TODO
    abort(404)

