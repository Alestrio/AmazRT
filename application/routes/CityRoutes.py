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
from application.data.entities.City import City


@app.route("/api/v1/city", methods=['GET'])
def getCities():
    city = session.query(City).all()
    return jsonify(city)


@app.route("/api/v1/city/<int: id_cit>", methods=['GET'])
def getCityByID(id_cit: int):
    city = session.query(City).all()
    for cit in city:
        if cit.id_city == id_cit:
            return jsonify(city)
    abort(404)


@app.route("/api/v1/city/<int: id_cit>", methods=['PUT'])
def updateCityByID(id_cit: int):
    city = session.query(City).update()
    for cit in city:
        if cit.id_city == id_cit:
            return jsonify(city) #TODO
    abort(404)


@app.route("/api/v1/city/<int: id_cit>", methods=['DELETE'])
def deleteCityByID(id_cit: int):
    city = session.query(City).delete()
    for cit in city:
        if cit.id_city == id_cit:
            return jsonify(city) #TODO
    abort(404)