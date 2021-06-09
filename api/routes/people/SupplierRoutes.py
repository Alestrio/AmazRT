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
from api.data.entities.people.Supplier import Supplier


@app.route("/api/v1/supplier", methods=['GET'])
@auth.login_required(role='operator')
def getSuppliers():
    suppliers = session.query(Supplier).all()
    return jsonify(suppliers)


@app.route("/api/v1/supplier/<int:id_sup>", methods=['GET'])
@auth.login_required(role='operator')
def getSupplierByID(id_sup: int):
    supplier = session.query(Supplier).filter_by(id_supplier=id_sup).first()
    if supplier is not None:
        return jsonify(supplier.todict())
    abort(404)


@app.route("/api/v1/supplier/<string:login>", methods=['GET'])
@auth.login_required(role=['operator', 'supplier'])
def getSupplierByLOGIN(login: str):
    supplier = session.query(Supplier).filter_by(login=login).first()
    if supplier is not None:
        return jsonify(supplier.todict())
    abort(404)


@app.route("/api/v1/supplier/<int:id_sup>", methods=['PUT'])
@auth.login_required(role='operator')
def updateSupplierByID(id_sup: int):
    supplier = session.query(Supplier).filter_by(id_supplier=id_sup).first()
    if supplier is not None:
        return jsonify(supplier)
    abort(404)


@app.route("/api/v1/supplier/<int:id_sup>", methods=['DELETE'])
@auth.login_required(role='operator')
def deleteSupplierByID(id_sup: int):
    supplier = session.query(Supplier).filter_by(id_supplier=id_sup).first()
    session.delete(supplier)
    abort(404)