import os
from app import create_app, db
from app.models import Voter, User, City
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager, Shell, Server


app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, Voter=Voter, User=User, City=City)

manager.add_command("runserver", Server(host='0.0.0.0'))
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()


__author__ = 'aftalavera'
