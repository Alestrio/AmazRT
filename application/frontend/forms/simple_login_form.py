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
    uname_field = StringField('uname', [InputRequired()], render_kw={"placeholder": "Enter Username"})
    password_field = PasswordField('Mot de passe', [InputRequired()], render_kw={"placeholder": "Enter Password"})
    submit = SubmitField('Se connecter !')
