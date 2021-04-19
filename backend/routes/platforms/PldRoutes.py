from flask import jsonify
from werkzeug.exceptions import abort

from backend import app
from backend.data.base import session
from backend.data.entities.platforms.Pld import Pld



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