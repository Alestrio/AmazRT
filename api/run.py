#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
import os

from flask import g, make_response, jsonify
from werkzeug.security import check_password_hash

from api import app, auth
from api.data.base import Base, engine, session
from api.data.entities.people.Customer import Customer
from api.data.entities.people.Operator import Operator
from api.data.entities.people.Supplier import Supplier


@auth.verify_password
def verify_password(u_login, password):
    user = {
        'as_customer': session.query(Customer).filter_by(login=u_login).first(),
        'as_operator': session.query(Operator).filter_by(login=u_login).first(),
        'as_supplier': session.query(Supplier).filter_by(login=u_login).first()
    }
    for i in user:
        if user[i] is not None and check_password_hash(user[i].password, password):
            g.current_user = user
            return user[i]
    return None


@auth.get_user_roles
def get_user_role(user):
    if isinstance(user, Customer):
        return 'customer'
    elif isinstance(user, Operator):
        return 'operator'
    elif isinstance(user, Supplier):
        return 'supplier'
    else:
        raise Exception('Unknown user role')


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


@app.errorhandler(404)
def custom_error(error):
    return make_response(jsonify({'error': str(error)}), 404)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
else:
    application = app
