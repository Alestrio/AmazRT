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
    ], render_kw={'id': 'register_radio'})
    supplier_id_field = StringField('supplier_id', [InputRequired()])
    customer_id_field = StringField('customer_id', [InputRequired()])
    pld_id_field = StringField('pld_id', [InputRequired()])
    submit = SubmitField('Envoyer !')