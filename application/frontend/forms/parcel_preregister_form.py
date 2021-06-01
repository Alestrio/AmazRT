#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, SelectField
from wtforms.validators import InputRequired


class PreRegisterForm(FlaskForm):
    source_country_field = SelectField('Pays', [InputRequired()], choices=[('fr', 'France')])
    source_city_field = StringField('Code postal/Ville', [InputRequired()])
    dest_country_field = SelectField('Pays', [InputRequired()], choices=[('fr', 'France')])
    dest_city_field = StringField('Code postal/Ville', [InputRequired()])
    parcel_type_field = RadioField('Type d\'envoi', choices=[('docs', 'Documents'), ('goods', 'Marchandises')])
    submit = SubmitField('Voir les offres')
