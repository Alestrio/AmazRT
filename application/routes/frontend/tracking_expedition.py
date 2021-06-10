#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
from flask import render_template, jsonify
from flask_login import current_user

from application import app, service
from application.data.entities.Parcel import Parcel
from application.data.entities.people.Customer import Customer
from application.data.entities.people.Supplier import Supplier
from application.frontend.forms.simple_login_form import SimpleLoginForm
from application.frontend.forms.simple_tracking_form import SimpleTrackingForm


def userTrackedParcels(user: Customer):
    cid = user.ide
    parcels = Parcel.fromdict(service.getWithPayload(Parcel(), {'id_user': cid}))
    parcel_array = []
    for i in parcels:
        parcel_array.append(i.todict())
    return parcel_array


def userTrackedParcelsSupplier(user: Supplier):
    cid = user.ide
    parcels = Parcel.fromdict(service.getWithPayload(Parcel(), {'id_supplier': cid}))
    parcel_array = []
    for i in parcels:
        parcel_array.append(i.todict())
    return parcel_array


@app.route('/tracking_expedition')
def tracking_expedition():
    if isinstance(current_user, Customer):
        user_parcels = userTrackedParcels(current_user)
        return render_template('pages/t_customer_trackingPage.html', login_form=SimpleLoginForm(),
                               user_tracked_parcels=user_parcels)
    elif isinstance(current_user, Supplier):
        user_parcels = userTrackedParcelsSupplier(current_user)
        return render_template('pages/t_customer_trackingPage.html', login_form=SimpleLoginForm(),
                               user_tracked_parcels=user_parcels)
    else:
        return render_template('pages/t_tracking_expedition.html', login_form=SimpleLoginForm(),
                               tracking_form=SimpleTrackingForm())
