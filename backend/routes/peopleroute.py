#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad

from flask import jsonify

from backend import app


@app.route("/")

@app.route("/customer/all")
def getCustomer():
    return "jsonify(service.findAll())"

@app.route("/customer/get")
def getCustomerByID():
    return "!"

@app.route("/customer/update")
def updateCustomerByID():
    return "!"

@app.route("/customer/delete")
def deleteCustomerByID():
    return "!"

@app.route("/operator/all")
def getOperator():
    return "!"

@app.route("/operator/get")
def getOperatorByID():
    return "!"

@app.route("/operator/update")
def updateCustomerByID():
    return "!"

@app.route("/operator/delete")
def deleteOperatorByID():
    return "!"

@app.route("/supplier/all")
def getSupplier():
    return "!"

@app.route("/supplier/get")
def getSupplierByID():
    return "!"

@app.route("/supplier/update")
def updateCustomerByID():
    return "!"

@app.route("/supplier/delete")
def deleteSupplierByID():
    return "!"

