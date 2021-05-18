#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad

from flask import request, flash, render_template
from flask_login import current_user, login_user
from werkzeug.utils import redirect

from application import app
from application.data.base import session
from application.data.entities.people.Customer import Customer
from application.data.entities.people.Operator import Operator
from application.data.entities.people.Supplier import Supplier
from application.frontend.forms.register_form import RegisterForm
from application.frontend.forms.simple_login_form import SimpleLoginForm


def create_customer(req):
    pass


def create_supplier(req):
    pass


def create_operator(req):
    pass


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
        u_login = request.form['login']
        user_type = request.form['type']
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

    else:
        return render_template('t_register.html', login_form=SimpleLoginForm(), register_form=RegisterForm())
