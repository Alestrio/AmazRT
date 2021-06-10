#    AmazRT  -  Parcel Management System
#    First semester Technical Degree project
#      Copyright  (c) 2021 - 2022
#     - Meryem KAYA @MeryemKy
#     - Alexis LEBEL @Alestrio
#     - Malo LEGRAND @HoesMaaad
from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, SubmitField, SelectField
from wtforms.validators import InputRequired


class SendTransmitForm(FlaskForm):
    type_radio = RadioField('type', [InputRequired()], choices=[
        ('send', 'Envoyer'),
        ('transmit', 'Transmettre'),
    ], render_kw={'id': 'type_radio'})
    plr_id_field = StringField('plr_id')
    pld_id_field = StringField('pld_id')
    dest_plr_field = StringField('dest_plr')
    parcel_field = StringField('id_colis')
    pld_to_plr_field = SelectField('pld_to_plr', choices=[
        ('pld_to_plr', 'D\'un PLD à un PLR'),
        ('plr_to_pld', 'D\'un PLR à un PLD')
    ])
    submit = SubmitField('Envoyer !')
