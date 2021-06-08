#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad

#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
from flask import jsonify, request
from werkzeug.exceptions import abort

from application import app
from application.data.base import session
from application.data.entities.people.Supplier import Supplier


@app.route("/api/v1/supplier", methods=['GET'])
def getSuppliers():
    suppliers = session.query(Supplier).all()
    return jsonify(suppliers)


@app.route("/api/v1/supplier/<int: id_sup>", methods=['GET'])
def getSupplierByID(id_sup: int):
    supplier = session.query(Supplier).filter_by(id_supplier=id_sup).first()
    if supplier is not None:
        return jsonify(supplier)
    abort(404)


@app.route("/api/v1/supplier/<int: id_sup>", methods=['PUT'])
def updateSupplierByID(id_sup: int):
    supplier = session.query(Supplier).filter_by(id_supplier=id_sup).first()
    if supplier is not None:
        return jsonify(supplier)
    abort(404)


@app.route("/api/v1/supplier/<int: id_sup>", methods=['DELETE'])
def deleteSupplierByID(id_sup: int):
    supplier = session.query(Supplier).filter_by(id_supplier=id_sup).first()
    new_data = request.get_json()
    if supplier is not None:
        supplier.id_city = new_data['id_city']
        supplier.ref = new_data['ref']
        supplier.name = new_data['name']
        supplier.address = new_data['address']
        supplier.login = new_data['login']
        supplier.password = new_data['password']
        session.query(Supplier).add()
    abort(404)