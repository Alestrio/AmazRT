#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import InputRequired


class PreRegisterForm(FlaskForm):
    source_country = StringField('Pays', [InputRequired()])
    source_city = StringField('Code postal/Ville', [InputRequired()])
    dest_country = StringField('Pays', [InputRequired()])
    dest_city = StringField('Code postal/Ville', [InputRequired()])
    documents = RadioField('Type d\'envoi', choices=[('docs', 'Documents'), ('goods', 'Marchandises')])
    submit = SubmitField('Voir les offres')
