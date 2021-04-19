from flask import jsonify
from werkzeug.exceptions import abort

from backend import app
from backend.data.base import session
from backend.data.entities.City import City



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