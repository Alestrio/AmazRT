#    AmazRT  -  Parcel Management System
#    First semester Technical Degree project
#      Copyright  (c) 2021 - 2022
#     - Meryem KAYA @MeryemKy
#     - Alexis LEBEL @Alestrio
#     - Malo LEGRAND @HoesMaaad
from flask import request, abort

from application import app
from application.data.base import session
from application.data.entities.Parcel import Parcel
from application.data.entities.actions.Leave import Leave
from application.data.entities.actions.Pull import Pull
from application.data.entities.actions.Send import Send
from application.data.entities.actions.Transmit import Transmit


def getAllPackageActions(tracking_number):
    parcel: Parcel = session.query(Parcel).filter_by(ref=tracking_number).first()
    if parcel is not None:
        leaves = session.query(Leave).filter_by(id_colis=parcel.id_parcel)
        pulls = session.query(Pull).filter_by(id_colis=parcel.id_parcel)
        sends = session.query(Send).filter_by(id_colis=parcel.id_parcel)
        transmits = session.query(Transmit).filter_by(id_colis=parcel.id_parcel)

        return {
            "parcel": parcel,
            "leaves": leaves,
            "pulls": pulls,
            "sends": sends,
            "transmits": transmits
        }
    abort(404)


@app.route('/track_parcel', methods=['GET'])
def track_parcel():
    settings = str(request.query_string).split('&')
    package_all_actions = getAllPackageActions(settings[0].split('=')[1])
