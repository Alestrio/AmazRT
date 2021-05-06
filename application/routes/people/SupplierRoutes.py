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
from flask import jsonify
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
    suppliers = session.query(Supplier).all()
    for sup in suppliers:
        if sup.id_supplier == id_sup:
            return jsonify(sup)
    abort(404)


@app.route("/api/v1/supplier/<int: id_sup>", methods=['PUT'])
def updateSupplierByID(id_sup: int):
    suppliers = session.query(Supplier).update()
    for sup in suppliers:
        if sup.id_supplier == id_sup:
            return jsonify(sup) #TODO
    abort(404)


@app.route("/api/v1/supplier/<int: id_sup>", methods=['DELETE'])
def deleteSupplierByID(id_sup: int):
    suppliers = session.query(Supplier).delete()
    for sup in suppliers:
        if sup.id_supplier == id_sup:
            return jsonify(sup) #TODO
    abort(404)