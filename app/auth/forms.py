from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import required, email


class LoginForm(Form):
    email = StringField('Email :', validators=[required('Please enter email.'), email()])
    password = PasswordField('Password :', validators=[required('Please enter password.')])
    submit = SubmitField('Login')





























__author__ = 'aftalavera'
