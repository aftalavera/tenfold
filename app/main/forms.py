from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, SelectField
from wtforms.validators import required, email
from ..models import Voter, User, City
from wtforms import ValidationError


class LoginForm(Form):
    email = StringField('Email :', validators=[required(), email()])
    password = PasswordField('Password :', validators=[required()])
    submit = SubmitField('Login')

    def validate_dpi(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('User with email already exists.')


class VoterForm(Form):

    dpi = StringField('DPI :', validators=[required('DPI is required.')])
    name = StringField('Name :', validators=[required('Name is required.')])
    email = StringField('Email :', validators=[required('Email is required.'), email()])
    phone = StringField('Phone :')
    city_id = SelectField('Location :', coerce=int)
    referred = TextAreaField('Referred :')
    submit = SubmitField('Save')

    def __init__(self, *args, **kwargs):
        super(VoterForm, self).__init__(*args, **kwargs)
        self.city_id.choices = [(city.id, city.department_nam + '/' + city.city_nam)
                                for city in City.query.order_by('department_nam', 'city_nam').all()]

    def validate_dpi(self, field):
        if Voter.query.filter_by(dpi=field.data).first():
            raise ValidationError('Voter with DPI already exists.')


class VoterEditForm(Form):

    dpi = StringField('DPI :', validators=[required('DPI is required.')])
    name = StringField('Name :', validators=[required('Name is required.')])
    email = StringField('Email :', validators=[required('Email is required.'), email()])
    phone = StringField('Phone :')
    city_id = SelectField('Location :', coerce=int)
    referred = TextAreaField('Referred :')
    submit = SubmitField('Save')

    def __init__(self, *args, **kwargs):
        super(VoterEditForm, self).__init__(*args, **kwargs)
        self.city_id.choices = [(city.id, city.department_nam + '/' + city.city_nam)
                                for city in City.query.order_by('department_nam', 'city_nam').all()]
        self.old_dpi = kwargs['obj'].dpi

    def validate_dpi(self, field):
        if Voter.query.filter_by(dpi=field.data).first() and self.dpi.data != self.old_dpi:
            raise ValidationError('Voter with DPI already exists.')




__author__ = 'aftalavera'

