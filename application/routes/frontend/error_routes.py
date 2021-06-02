#    AmazRT  -  Parcel Management System
#    First semester Technical Degree project
#      Copyright  (c) 2021 - 2022
#     - Meryem KAYA @MeryemKy
#     - Alexis LEBEL @Alestrio
#     - Malo LEGRAND @HoesMaaad
import werkzeug.exceptions
from flask import render_template

from application import app


@app.errorhandler(werkzeug.exceptions.Forbidden)
def forbidden(reason):
    return render_template('errors/e_forbidden.html')


@app.errorhandler(werkzeug.exceptions.NotFound)
def not_found(reason):
    return render_template('errors/e_not_found.html')


@app.errorhandler(werkzeug.exceptions.BadRequest)
def bad_request(reason):
    return render_template('errors/e_bad_request.html')
