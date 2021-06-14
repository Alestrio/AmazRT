#    AmazRT  -  Parcel Management System
#    First semester Technical Degree project
#      Copyright  (c) 2021 - 2022
#     - Meryem KAYA @MeryemKy
#     - Alexis LEBEL @Alestrio
#     - Malo LEGRAND @HoesMaaad
import datetime
import random
import string

from flask import render_template, request, redirect
from flask_login import current_user
from werkzeug.exceptions import abort

from application import app, service
from application.data.JsonParcelService import JsonParcelService
from application.data.data_classes.TripStage import LocationType
from application.data.entities.Parcel import Parcel
from application.data.entities.actions.Leave import Leave
from application.data.entities.actions.Send import Send
from application.data.entities.actions.Transmit import Transmit
from application.data.entities.people.Customer import Customer
from application.data.entities.people.Operator import Operator
from application.data.entities.people.Supplier import Supplier
from application.frontend.forms.parcel_register_form import ParcelRegisterForm
from application.frontend.forms.register_form import RegisterForm
from application.frontend.forms.send_transmit_form import SendTransmitForm
from application.frontend.forms.simple_login_form import SimpleLoginForm


@app.route('/parcel-register', methods=['GET', 'POST'])
def parcel_register():
    if request.method == 'GET':
        if isinstance(current_user, Operator):
            tolist = []
            # allUsers = session.query(Customer).all()
            allUsers = Customer.fromdict(service.getall(Customer()))
            for i in allUsers:
                tolist.append(i.todict())
            return render_template('pages/t_parcel_register.html', parcel_register_form=ParcelRegisterForm(),
                                   userdata=tolist, register_form=RegisterForm())
        else:
            abort(403)
    elif request.method == 'POST':
        data = request.form

        supplier_test = Supplier.fromdict(service.getOne(Supplier(), data['supplier_id_field']))
        customer_test = Customer.fromdict(service.getOne(Customer(), data['customer_id_field']))

        if supplier_test is None or customer_test is None or data['type_radio'] == '':
            abort(400)

        # Generates random reference :
        rand_ref = (data['type_radio'][0].upper() + datetime.date.today().strftime('%y%d%m'))
        for i in range(4):
            rand_ref += random.choice(string.ascii_letters)
        rand_ref = rand_ref.upper()

        datadict = {
            "type": data['type_radio'],
            "supplier_id": data['supplier_id_field'],
            "customer_id": data['customer_id_field'],
            "ref": rand_ref,
            "pld_id": data['pld_id_field']
        }

        parcel = Parcel(0, datadict['ref'], datadict['type'], datadict['customer_id'], datadict['supplier_id'])
        service.add(parcel)
        # parcel = session.query(Parcel).filter_by(ref=datadict['ref']).first()
        parcel = Parcel.fromdict(service.getOne(Parcel(), datadict['ref']))
        leave = Leave(parcel.ide, datadict['pld_id'], datadict['supplier_id'], datetime.datetime.now())
        service.add(leave)
        json_service = JsonParcelService()
        json_service.createParcel(Parcel.fromdict(service.getOne(Parcel(), rand_ref)))
        return redirect('/')
    else:
        abort(502)


@app.route('/send-transmit', methods=['GET', 'POST'])
def send_transmit():
    if request.method == 'GET':
        if isinstance(current_user, Operator):
            return render_template('pages/t_send_transmit.html', login_form=SimpleLoginForm(),
                                   send_transmit_form=SendTransmitForm())
        else:
            abort(403)
    elif request.method == 'POST':
        data = request.form
        if data['type_radio'] == 'send':
            datadict = {
                'parcel': data['parcel_field'],
                'pld': data['pld_id_field'],
                'plr': data['plr_id_field'],
                'send_date': datetime.datetime.now().timestamp(),
                'reception_date': datetime.datetime.fromtimestamp(0).timestamp(),
                'pld_to_plr': (False, True)[data['pld_to_plr_field'] == 'pld_to_plr']
            }
            send = Send.fromdict(datadict)
            service.add(send)
            json_service = JsonParcelService()
            json_service.moveParcel(Parcel.fromdict(service.getOne(Parcel(), data['parcel_field'])),
                                    (LocationType.PLD, LocationType.PLR)[data['pld_to_plr_field'] == 'pld_to_plr'],
                                    (data['pld_id_field'], data['plr_id_field'])[data['pld_to_plr_field']
                                                                                 == 'pld_to_plr'])
        elif data['type_radio'] == 'transmit':
            datadict = {
                'parcel': data['parcel_field'],
                'plr': data['plr_id_field'],
                'dest_plr': data['dest_plr_field'],
                'send_date': datetime.datetime.now().timestamp(),
                'reception_date': datetime.datetime.fromtimestamp(0).timestamp()
            }
            transmit = Transmit.fromdict(datadict)
            #service.add(transmit)
            json_service = JsonParcelService()
            json_service.moveParcel(Parcel.fromdict(service.getOne(Parcel(), data['parcel_field'])),
                                    LocationType.PLR, data['dest_plr_field'])
        return redirect('/send-transmit')
    else:
        abort(502)
