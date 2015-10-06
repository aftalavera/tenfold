from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from . import db, login_manager


class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    dpi = db.Column(db.String(15), unique=True)
    name = db.Column(db.String(50))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(128))
    user_voters = db.relationship('Voter', backref='user')

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Voter(db.Model):

    __tablename__ = 'voters'

    id = db.Column(db.Integer, primary_key=True)
    dpi = db.Column(db.String(15), unique=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    department = db.Column(db.String(100))
    city = db.Column(db.String(100))
    referred = db.Column(db.Text)
    voted = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))


class City(db.Model):

    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    department_code = db.Column(db.Integer)
    department_nam = db.Column(db.String(100))
    city_code = db.Column(db.Integer)
    city_nam = db.Column(db.String(100))
    city_voters = db.relationship('Voter')

__author__ = 'aftalavera'
