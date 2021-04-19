#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
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
from application.data.entities.platforms.Pld import Pld

app.route("/api/v1/pld", methods=['GET'])


def getPld():
    pld = session.query(Pld).all()
    return jsonify(pld)


@app.route("/api/v1/pld/<int: id_pld>", methods=['GET'])
def getPldByID(id_pld: int):
    pld = session.query(Pld).all()
    for pld in pld:
        if pld.id_parcel == id_pld:
            return jsonify(pld)
    abort(404)