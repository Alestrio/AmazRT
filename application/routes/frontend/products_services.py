#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
from flask import render_template

from application import app
from application.frontend.forms.simple_login_form import SimpleLoginForm


@app.route('/products_services')
def products_services():
    return render_template('t_products_services.html', login_form=SimpleLoginForm())
