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
from application.data.entities.platforms.Plr import Plr

app.route("/api/v1/plr", methods=['GET'])


def getPlr():
    plr = session.query(Plr).all()
    return jsonify(plr)


@app.route("/api/v1/plr/<int: id_plr>", methods=['GET'])
def getPlrByID(id_plr: int):
    plr = session.query(Plr).all()
    for plr in plr:
        if plr.id_plr == id_plr:
            return jsonify(plr)
    abort(404)