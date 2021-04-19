#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad

#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
from flask import render_template

from application import app


@app.route('/products_services')
def products_services():
    return render_template('t_products_services.html')
