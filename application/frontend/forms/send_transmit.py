#    AmazRT  -  Parcel Management System
#    First semester Technical Degree project
#      Copyright  (c) 2021 - 2022
#     - Meryem KAYA @MeryemKy
#     - Alexis LEBEL @Alestrio
#     - Malo LEGRAND @HoesMaaad
from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, SubmitField
from wtforms.validators import InputRequired


class SendTransmitForm(FlaskForm):
    type_radio = RadioField('type', [InputRequired()], choices=[
        ('send', 'Envoyer'),
        ('transmit', 'Transmettre'),
    ], render_kw={'id': 'register_radio'})
    plr_id_field = StringField('plr_id', [InputRequired()])
    pld_id_field = StringField('pld_id', [InputRequired()])
    dest_plr_field = StringField('plr_id_plr', [InputRequired()])
    parcel_field = StringField('id_colis', [InputRequired()])
    pld_to_plr_field = StringField('pld_to_plr', [InputRequired()])
    submit = SubmitField('Envoyer !')