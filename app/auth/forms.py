from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import required, email
from ..models import City
from .. import db


class LoginForm(Form):
    email = StringField('Email :', validators=[required('Please enter email.'), email()])
    password = PasswordField('Password :', validators=[required('Please enter password.')])
    # department = SelectField('Department :', coerce=int)
    submit = SubmitField('Login')

    # def __init__(self, *args, **kwargs):
    #     super(LoginForm, self).__init__(*args, **kwargs)
    #     query = db.session.query(City.department_nam.distinct().label("department"))
    #     # self.department.choices = [(1, row.department) for row in query.order_by('department').all()]
    #     self.department.choices = [(1, 'San Juan')]





























__author__ = 'aftalavera'
