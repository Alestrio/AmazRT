#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
import random

from flask import render_template, request, abort

from application import app
from application.data.base import session
from application.data.entities.City import City
from application.frontend.forms.parcel_preregister_form import PreRegisterForm
from application.frontend.forms.simple_login_form import SimpleLoginForm
from application.frontend.forms.simple_tracking_form import SimpleTrackingForm


@app.route('/')
def index():
    return render_template('t_index.html', login_form=SimpleLoginForm(), tracking_form=SimpleTrackingForm(),
                           preregister_form=PreRegisterForm())


@app.route('/preregister', methods=['POST'])
def preregister():
    data = request.form
    datadict = {
        "source_country": data['source_country_field'],
        "source_city": data['source_city_field'],
        "dest_country": data['dest_country_field'],
        "dest_city": data['dest_city_field'],
        "parcel_type": data['parcel_type_field'],
        "invoice_price": random.randint(15, 64),
        "source_city_id": None,
        "dest_city_id": None
    }  # Again, we are wrapping the data in a dict to provide data as one object to Jinja

    source_city_id = session.query(City).filter_by(name=datadict['source_city']).first()
    dest_city_id = session.query(City).filter_by(name=datadict['dest_city']).first()

    if source_city_id is None or dest_city_id is None:
        abort(400)

    datadict['source_city_id'] = source_city_id.id_city
    datadict['dest_city_id'] = dest_city_id.id_city

    return render_template('t_expedition_invoice.html', data=datadict, login_form=SimpleLoginForm())
