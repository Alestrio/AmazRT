#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired


class SimpleLoginForm(FlaskForm):
    email_field = StringField('email', [InputRequired()])
    password_field = PasswordField('Mot de passe', [InputRequired()])
    submit = SubmitField('Se connecter !')
