#    AmazRT  -  Parcel Management System
#    First semester Technical Degree project
#      Copyright  (c) 2021 - 2022
#     - Meryem KAYA @MeryemKy
#     - Alexis LEBEL @Alestrio
#     - Malo LEGRAND @HoesMaaad
import datetime
import random
import string

from flask import render_template, jsonify, request, redirect
from flask_login import current_user
from werkzeug.exceptions import abort

from application import app
from application.data.base import session
from application.data.entities.Parcel import Parcel
from application.data.entities.actions.Leave import Leave
from application.data.entities.people.Customer import Customer, todict
from application.data.entities.people.Operator import Operator
from application.data.entities.people.Supplier import Supplier
from application.frontend.forms.parcel_register_form import ParcelRegisterForm
from application.frontend.forms.send_transmit import SendTransmitForm
from application.frontend.forms.simple_login_form import SimpleLoginForm


@app.route('/parcel-register', methods=['GET', 'POST'])
def parcel_register():
    if request.method == 'GET':
        if isinstance(current_user, Operator):
            tolist = []
            allUsers = session.query(Customer).all()
            for i in allUsers:
                tolist.append(todict(i))
            return render_template('pages/t_parcel_register.html', register_form=ParcelRegisterForm(),
                                   userdata=tolist)
        else:
            abort(403)
    elif request.method == 'POST':
        data = request.form

        supplier_test = session.query(Supplier).filter_by(id_supplier=data['supplier_id_field']).first()
        customer_test = session.query(Customer).filter_by(id_client=data['customer_id_field']).first()

        if supplier_test is None or customer_test is None or data['type_radio'] == '':
            abort(400)

        # Generates random reference :
        rand_ref = ''
        for i in range(10):
            rand_ref += random.choice(string.ascii_letters)
        rand_ref = rand_ref.upper()

        datadict = {
            "type": data['type_radio'],
            "supplier_id": data['supplier_id_field'],
            "customer_id": data['customer_id_field'],
            "ref": rand_ref,
            "pld_id": data['pld_id_field']
        }

        parcel = Parcel(datadict['ref'], datadict['type'], datadict['customer_id'], datadict['supplier_id'])
        session.add(parcel)
        session.commit()
        parcel = session.query(Parcel).filter_by(ref=datadict['ref']).first()
        leave = Leave(parcel.id_parcel, datadict['pld_id'], datadict['supplier_id'], datetime.datetime.now())
        session.add(leave)
        session.commit()
        return redirect('/')
    else:
        abort(502)

@app.route('/send-transmit', methods=['GET', 'POST']')
def send_transmit():
        if isinstance(current_user, Operator):
            tolist = []
            allUsers = session.query(Customer).all()
            for i in allUsers:
                tolist.append(todict(i))
            return render_template('pages/t_send_transmit.html', login_form=SimpleLoginForm(),
                                   send_transmit_form=SendTransmitForm())
        else:
            abort(403)
    elif request.method == 'POST':
        data = request.form

        supplier_test = session.query(Supplier).filter_by(id_supplier=data['supplier_id_field']).first()
        customer_test = session.query(Customer).filter_by(id_client=data['customer_id_field']).first()

        if supplier_test is None or customer_test is None or data['type_radio'] == '':
            abort(400)

        # Generates random reference :
        rand_ref = ''
        for i in range(10):
            rand_ref += random.choice(string.ascii_letters)
        rand_ref = rand_ref.upper()

        datadict = {
            "type": data['type_radio'],
            "supplier_id": data['supplier_id_field'],
            "customer_id": data['customer_id_field'],
            "ref": rand_ref,
            "pld_id": data['pld_id_field']
        }

        parcel = Parcel(datadict['ref'], datadict['type'], datadict['customer_id'], datadict['supplier_id'])
        session.add(parcel)
        session.commit()
        parcel = session.query(Parcel).filter_by(ref=datadict['ref']).first()
        leave = Leave(parcel.id_parcel, datadict['pld_id'], datadict['supplier_id'], datetime.datetime.now())
        session.add(leave)
        session.commit()
        return redirect('/')
    else:
        abort(502)