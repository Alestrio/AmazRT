#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
from flask import jsonify
from werkzeug.exceptions import abort

from api import auth
from api import app
from api.data.base import session
from api.data.entities.City import City


@app.route("/api/v1/city", methods=['GET'])
@auth.login_required(['operator', 'supplier', 'customer'])
def getCities():
    city = session.query(City).all()
    return jsonify(city)


@app.route("/api/v1/city/<int:id_city>", methods=['GET'])
@auth.login_required(['operator', 'supplier', 'customer'])
def getCityByID(id_city: int):
    city = session.query(City).all()
    for cit in city:
        if cit.id_city == id_city:
            return jsonify(city)
    abort(404)


@app.route("/api/v1/city/<string:name_city>", methods=['GET'])
@auth.login_required(['operator', 'supplier', 'customer'])
def getCityByNAME(name_city: str):
    city = session.query(City).filter_by(name=name_city).first()
    if city:
        return jsonify(city.todict())
    abort(404)


@app.route("/api/v1/city/<int:id_city>", methods=['PUT'])
@auth.login_required('operator')
def updateCityByID(id_city: int):
    city = session.query(City).update()
    for cit in city:
        if cit.id_city == id_city:
            return jsonify(city)  # TODO
    abort(404)


@app.route("/api/v1/city/<int:id_city>", methods=['DELETE'])
@auth.login_required('operator')
def deleteCityByID(id_city: int):
    city = session.query(City).filter_by(id_city=id_city)
    try:
        session.delete(city)
        session.commit()
    except Exception:
        abort(404)
