#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
from flask import render_template

from application import app
from application.frontend.forms.simple_login_form import SimpleLoginForm


@app.route('/')
def index():
    return render_template('t_index.html', login_form=SimpleLoginForm())
