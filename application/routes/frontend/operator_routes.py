#    AmazRT  -  Parcel Management System
#    First semester Technical Degree project
#      Copyright  (c) 2021 - 2022
#     - Meryem KAYA @MeryemKy
#     - Alexis LEBEL @Alestrio
#     - Malo LEGRAND @HoesMaaad
from flask import render_template, jsonify, request
from flask_login import current_user
from werkzeug.exceptions import abort

from application import app
from application.data.base import session
from application.data.entities.people.Customer import Customer, todict
from application.data.entities.people.Operator import Operator
from application.frontend.forms.parcel_register_form import ParcelRegisterForm


@app.route('/parcel-register', methods=['GET', 'POST'])
def parcel_register():
    if request.method == 'GET':
        if isinstance(current_user, Operator):
            tolist = []
            allUsers = session.query(Customer).all()
            for i in allUsers:
                tolist.append(todict(i))
            return render_template('t_parcel_register.html', register_form=ParcelRegisterForm(),
                                   userdata=tolist)
        else:
            abort(403)
    elif request.method == 'POST':
        pass
    else:
        abort(502)
