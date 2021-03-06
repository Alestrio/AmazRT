#    AmazRT  -  Parcel Management System
#    First semester Technical Degree project
#      Copyright  (c) 2021 - 2022
#     - Meryem KAYA @MeryemKy
#     - Alexis LEBEL @Alestrio
#     - Malo LEGRAND @HoesMaaad
from flask import request, abort, jsonify, render_template

from application import app, service
from application.data.data_classes.TripStage import TripStageType
from application.data.data_classes import TripStage
from application.data.entities.Parcel import Parcel
from application.data.entities.actions.Leave import Leave
from application.data.entities.actions.Pull import Pull
from application.data.entities.actions.Send import Send
from application.data.entities.actions.Transmit import Transmit
from application.frontend.forms.simple_login_form import SimpleLoginForm


def getAllPackageActions(tracking_number):
    parcel: Parcel = Parcel.fromdict(service.getOne(Parcel(), tracking_number))
    if parcel is not None:
        leave = Leave.fromdict(service.getOne(Leave(), parcel.ref))  # those are intended to be unique
        # that's why we are taking the first element
        pull = Pull.fromdict(service.getOne(Pull(), parcel.ref))
        sends = Send.fromdict(service.getOne(Send(), parcel.ref))
        transmits = Transmit.fromdict(service.getOne(Transmit(), parcel.ref))

        return {
            "parcel": parcel,
            TripStageType.LEAVE: leave,
            TripStageType.PULL: pull,
            TripStageType.SEND: sends,
            TripStageType.TRANSMIT: transmits
        }
    abort(404)


@app.route('/track_parcel', methods=['GET'])
def track_parcel():
    settings = str(request.query_string).split('&')
    package_all_actions = getAllPackageActions(settings[0].split('=')[1])  # This is ugly, but it works

    package_trip = [TripStage.from_leave(package_all_actions[TripStageType.LEAVE])]
    j = 1
    if package_all_actions[TripStageType.SEND] is not None:
        for i in package_all_actions[TripStageType.SEND]:
            package_trip.append(TripStage.from_send(j, i))
            j += 1
    if package_all_actions[TripStageType.TRANSMIT] is not None:
        for i in package_all_actions[TripStageType.TRANSMIT]:
            package_trip.append(TripStage.from_transmit(j, i))
            j += 1
    if package_all_actions[TripStageType.PULL] is not None:
        package_trip.append(TripStage.from_pull(j, package_all_actions[TripStageType.PULL]))

    #ordered = TripStage.orderByDate(package_trip)
    tripstages = []
    for i in package_trip:
        tripstages.append(i.__dict__())
    return render_template('pages/t_parcel_tracking.html', tripstages=tripstages, login_form=SimpleLoginForm())
