#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
from flask import request, flash, render_template
from flask_login import current_user, login_user, LoginManager
from werkzeug.utils import redirect

from application import app
from application.data.base import session
from application.data.entities.people.Customer import Customer
from application.data.entities.people.Operator import Operator
from application.data.entities.people.Supplier import Supplier

login = LoginManager()


def create_customer(email, username, password):
    pass


def create_supplier(email, username, password):
    pass


def create_operator(email, username, password):
    pass


@login.user_loader
def load_user(user_id):
    user = {
        'as_customer': Customer.query.filter_by(id=user_id).first(),
        'as_operator': Operator.query.filter_by(id=user_id).first(),
        'as_supplier': Supplier.query.filter_by(id=user_id).first()
    }
    for i in user:
        if user[i] is not None:
            return user[i]
    return None


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        user = {
            'as_customer': Customer.query.filter_by(email=email).first(),
            'as_operator': Operator.query.filter_by(email=email).first(),
            'as_supplier': Supplier.query.filter_by(email=email).first()
        }
        for i in user:
            if user[i] is not None and user[i].check_password(request.form['password']):
                login_user(user[i])
    return redirect('/')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        user_type = request.form['type']

        user = {
            'as_customer': Customer.query.filter_by(email=email).first(),
            'as_operator': Operator.query.filter_by(email=email).first(),
            'as_supplier': Supplier.query.filter_by(email=email).first()
        }
        for i in user:
            if user[i] is not None and user[i].check_password(request.form['password']):
                flash("Cet utilisateur existe déjà !")

        user_creator = {
            'customer': create_customer,
            'operator': create_operator,
            'supplier': create_supplier
        }
        user_creator[user_type](email, username, password)
        session.add(user)
        session.commit()
        return redirect('/login')
    return render_template('register.html')
