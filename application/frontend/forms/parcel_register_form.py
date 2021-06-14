#    AmazRT  -  Parcel Management System
#    First semester Technical Degree project
#      Copyright  (c) 2021 - 2022
#     - Meryem KAYA @MeryemKy
#     - Alexis LEBEL @Alestrio
#     - Malo LEGRAND @HoesMaaad
from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, SubmitField
from wtforms.validators import InputRequired


class ParcelRegisterForm(FlaskForm):
    type_radio = RadioField('type', [InputRequired()], choices=[
        ('documents', 'Documents'),
        ('goods', 'Marchandises'),
    ], render_kw={'id': 'type_radio'})
    parcel_trip_type = RadioField('parcel_trip', [InputRequired()], choices=[
        ('city-to-city', 'D\'une ville à une autre'),
        ('supplier-to-customer', 'D\'un fournisseur à un client')
    ])
    supplier_id_field = StringField('supplier_id')
    source_city_field = StringField('source_city')
    customer_id_field = StringField('customer_id')
    dest_city_field = StringField('dest_city')
    pld_id_field = StringField('pld_id', [InputRequired()])
    submit = SubmitField('Envoyer !')
