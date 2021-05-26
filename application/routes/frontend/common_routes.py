#    AmazRT  -  Parcel Management System
#    First semester Technical Degree project
#      Copyright  (c) 2021 - 2022
#     - Meryem KAYA @MeryemKy
#     - Alexis LEBEL @Alestrio
#     - Malo LEGRAND @HoesMaaad
import random
import string

from flask import request, flash, render_template, abort
from flask_login import current_user, login_user
from werkzeug.utils import redirect

from application import app
from application.data.base import session
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
        city_id = session.query(City).filter_by(name=address_field).first()
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

    # Generates random reference :
    rand_ref = ''
    for i in range(10):
        rand_ref += random.choice(string.ascii_letters)
    rand_ref = rand_ref.upper()

    if data is not None:
        customer = Customer(data['city_id'], rand_ref, data['lastname'], data['firstname'],
                            data['login'], data['password'])
        customer.hash_password()
        session.add(customer)
        session.commit()


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
        city_id = session.query(City).filter_by(name=address_field).first()
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

    # Generates random reference :
    rand_ref = ''
    for i in range(10):
        rand_ref += random.choice(string.ascii_letters)
    rand_ref = rand_ref.upper()

    if data is not None:
        supplier = Supplier(data['city_id'], rand_ref, data['lastname'] + " " + data['firstname'],
                            data['login'], data['password'], data['activity'])
        supplier.hash_password()
        session.add(supplier)
        session.commit()


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

    # Generates random reference :
    rand_ref = ''
    for i in range(10):
        rand_ref += random.choice(string.ascii_letters)
    rand_ref = rand_ref.upper()

    if data is not None:
        operator = Operator(data['id_pld'], data['lastname'], data['firstname'],
                            data['login'], data['password'], rand_ref)
        operator.hash_password()
        session.add(operator)
        session.commit()


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        u_login = request.form['uname_field']
        user = {
            'as_customer': session.query(Customer).filter_by(login=u_login).first(),
            'as_operator': session.query(Operator).filter_by(login=u_login).first(),
            'as_supplier': session.query(Supplier).filter_by(login=u_login).first()
        }
        for i in user:
            if user[i] is not None and user[i].check_password(request.form['password_field']):
                login_user(user[i])
    return redirect('/')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        u_login = request.form['login_field']
        user_type = request.form['user_type_field']
        user = {
            'as_customer': session.query(Customer).filter_by(login=u_login).first(),
            'as_operator': session.query(Operator).filter_by(login=u_login).first(),
            'as_supplier': session.query(Supplier).filter_by(login=u_login).first()
        }
        for i in user:
            if user[i] is not None:
                flash("Cet utilisateur existe déjà !")

        user_creator = {
            'customer': create_customer,
            'operator': create_operator,
            'supplier': create_supplier
        }
        user_creator[user_type](request)
        return redirect('/')

    else:
        return render_template('t_register.html', login_form=SimpleLoginForm(), register_form=RegisterForm())
