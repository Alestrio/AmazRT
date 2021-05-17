#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad
from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, PasswordField
from wtforms.validators import InputRequired


class RegisterForm(FlaskForm):
    user_type_field = RadioField('type', [InputRequired()], choices=[
        ('customer', 'Je suis un Client !'),
        ('operator', 'Je suis un Opérateur (et j\'ai réussi mon entretien d\'embauche !)'),
        ('supplier', 'Je suis un Fournisseur ! (De produits légaux !)')
    ], render_kw={'id': 'register_radio'})

    # Those are common fields for users
    firstname_field = StringField('firstname', InputRequired(),
                                  render_kw={"placeholder": "Enter your firstname"})
    lastname_field = StringField('lastname', render_kw={"placeholder": "Enter youtr lastname"})
    login_field = StringField('login', InputRequired(), render_kw={"placeholder": "Enter your login"})
    password_field = PasswordField('password', InputRequired(), render_kw={"placeholder": "Enter your password"})
    confirm_password_field = PasswordField('confirm_password', InputRequired(),
                                           render_kw={"placeholder": "Confirm your password"})

    # Those are fields for customer and suppliers
    address_field = StringField('address', InputRequired(),
                                render_kw={'id': 'register_address', "placeholder": "Enter your city name"})

    # Those are supplier-only fields
    activity_field = StringField('activity',
                                 render_kw={'id': 'register_activity', "placeholder": "Enter your activity"})
