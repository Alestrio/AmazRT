#    AmazRT  -  Parcel Management System
#    First semester Technical Degree project
#      Copyright  (c) 2021 - 2022
#     - Meryem KAYA @MeryemKy
#     - Alexis LEBEL @Alestrio
#     - Malo LEGRAND @HoesMaaad
import datetime
import random
import string

from flask import request, flash, render_template, abort, session
from flask_login import current_user, login_user, logout_user
from requests.auth import HTTPBasicAuth
from werkzeug.utils import redirect

from application import app, service
from application.data.entities.City import City
from application.data.entities.people.Customer import Customer
from application.data.entities.people.Operator import Operator
from application.data.entities.people.Supplier import Supplier
from application.frontend.forms.register_form import RegisterForm
from application.frontend.forms.simple_login_form import SimpleLoginForm


def sanity_check_customer_request(req):
    firstname_field = req.form['firstname_field']
    lastname_field = req.form['lastname_field']
    login_field = req.form['login_field']
    password_field = req.form['password_field']
    confirm_password_field = req.form['confirm_password_field']
    address_field = req.form['address_field']

    if (firstname_field is not None and
            lastname_field is not None and
            login_field is not None and
            password_field is not None and password_field == confirm_password_field and
            address_field is not None):
        # city_id = session.query(City).filter_by(name=address_field).first()
        city_id = City.fromdict(service.getOne(City, address_field))
        city_id = city_id.id_city
        if city_id is not None:
            return {
                "firstname": firstname_field,
                "lastname": lastname_field,
                "login": login_field,
                "password": password_field,
                "city_id": city_id
            }
    abort(400)


def create_customer(req):
    data = sanity_check_customer_request(req)

    if data is not None:
        # Generates random reference :
        rand_ref = 'C' + str(data['lastname']).lower().replace(r'[_\s]', '') + datetime.date.today().strftime('%y%d%m')
        for i in range(4):
            rand_ref += random.choice(string.ascii_letters)
        rand_ref = rand_ref.upper()

        customer = Customer(0, data['city_id'], rand_ref, data['lastname'], data['firstname'],
                            data['login'], data['password'])
        service.add(customer)


def sanity_check_supplier_request(req):
    firstname_field = req.form['firstname_field']
    lastname_field = req.form['lastname_field']
    login_field = req.form['login_field']
    password_field = req.form['password_field']
    confirm_password_field = req.form['confirm_password_field']
    address_field = req.form['address_field']
    activity_field = req.form['activity_field']

    if (firstname_field is not None and
            login_field is not None and
            password_field is not None and password_field == confirm_password_field and
            address_field is not None and
            activity_field is not None):
        # city_id = session.query(City).filter_by(name=address_field).first()
        city_id = City.fromdict(City.filter_by(service.getall(City()), name=address_field))
        city_id = city_id.id_city
        if city_id is not None:
            return {
                "firstname": firstname_field,
                "lastname": lastname_field,
                "login": login_field,
                "password": password_field,
                "city_id": city_id,
                "activity": activity_field
            }
    abort(400)


def create_supplier(req):
    data = sanity_check_supplier_request(req)

    if data is not None:
        # Generates random reference :
        rand_ref = 'S' + str(data['lastname']).lower().replace(r'[_\s]', '') + datetime.date.today().strftime('%y%d%m')
        for i in range(4):
            rand_ref += random.choice(string.ascii_letters)
        rand_ref = rand_ref.upper()

        supplier = Supplier(0, data['city_id'], rand_ref, data['lastname'] + " " + data['firstname'],
                            data['login'], data['password'], data['activity'])
        service.add(supplier)


def sanity_check_operator_request(req):
    firstname_field = req.form['firstname_field']
    lastname_field = req.form['lastname_field']
    login_field = req.form['login_field']
    password_field = req.form['password_field']
    confirm_password_field = req.form['confirm_password_field']
    id_pld_field = req.form['id_pld_field']

    if (firstname_field is not None and
            lastname_field is not None and
            login_field is not None and
            password_field is not None and password_field == confirm_password_field and
            id_pld_field is not None):
        return {
            "id_pld": id_pld_field,
            "firstname": firstname_field,
            "lastname": lastname_field,
            "login": login_field,
            "password": password_field,
        }
    abort(400)


def create_operator(req):
    data = sanity_check_operator_request(req)

    if data is not None:
        # Generates random reference :
        rand_ref = 'O' + str(data['lastname']).lower().replace(r'[_\s]', '') + datetime.date.today().strftime('%y%d%m')
        for i in range(4):
            rand_ref += random.choice(string.ascii_letters)
        rand_ref = rand_ref.upper()

        operator = Operator(0, data['id_pld'], data['lastname'], data['firstname'],
                            data['login'], data['password'], rand_ref)
        service.add(operator)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        u_login = request.form['uname_field']
        u_pass = request.form['password_field']
        user = {
            'as_customer': Customer.fromdict(service.getOneSupplyAuth(Customer(),
                                                                      u_login, HTTPBasicAuth(u_login, u_pass))),
            'as_operator': Operator.fromdict(service.getOneSupplyAuth(Operator(),
                                                                      u_login, HTTPBasicAuth(u_login, u_pass))),
            'as_supplier': Supplier.fromdict(service.getOneSupplyAuth(Supplier(),
                                                                      u_login, HTTPBasicAuth(u_login, u_pass)))
        }
        for i in user:
            if user[i] is not None and user[i].check_password(request.form['password_field']):
                login_user(user[i])
                service.user = user[i]
                service.user.password = request.form['password_field']
    return redirect('/')


@app.route('/logout')
def logout():
    logout_user()
    service.user = None
    return redirect('/')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        u_login = request.form['login_field']
        user_type = request.form['user_type_field']
        exists = service.checkIfLoginExists(u_login)
        user_creator = {
            'customer': create_customer,
            'operator': create_operator,
            'supplier': create_supplier
        }
        user_creator[user_type](request)
        return redirect('/')

    else:
        return render_template('pages/t_register.html', login_form=SimpleLoginForm(), register_form=RegisterForm())
