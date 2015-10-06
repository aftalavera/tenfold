import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'me picala jaiba'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://tenfold:pipe@sdipr.net/tenfold'



config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,

}

__author__ = 'aftalavera'
