#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
import os

from flask_login import LoginManager
from flask_wtf import CSRFProtect
from flask_qrcode import QRcode
from flask import session
from requests.auth import HTTPBasicAuth

from application import app, service
from application.data.entities.people.Customer import Customer
from application.data.entities.people.Operator import Operator
from application.data.entities.people.Supplier import Supplier

login = LoginManager()


@login.user_loader
def load_user(u_login):
    user = {
        'as_customer': Customer.fromdict(service.getOne(Customer(), u_login)),
        'as_operator': Operator.fromdict(service.getOne(Operator(), u_login)),
        'as_supplier': Supplier.fromdict(service.getOne(Supplier(), u_login))
    }
    for i in user:
        if user[i] is not None:
            return user[i]
    return None


if __name__ == "__main__":
    csrf = CSRFProtect(app)
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['WTF_CSRF_SECRET_KEY'] = SECRET_KEY
    csrf.init_app(app)
    login.init_app(app)
    QRcode(app)
    app.run(debug=True, port=80)
else:
    csrf = CSRFProtect(app)
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['WTF_CSRF_SECRET_KEY'] = SECRET_KEY
    csrf.init_app(app)
    login.init_app(app)
    QRcode(app)
    application = app
