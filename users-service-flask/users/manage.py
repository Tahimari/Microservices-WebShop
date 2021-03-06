import sys
import unittest
import coverage

from flask.cli import FlaskGroup
from project import create_app, db
from project.api.models import User

COV = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'project/tests/*',
        'project/config.py',
    ]
)
COV.start()

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command()
def test():
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    sys.exit(result)

@cli.command('seed_db')
def seed_db():
    db.session.add(User(email="hermanmu@gmail.com", first_name='asdasd', last_name='Bca123', password='Abc123'))
    db.session.add(User(email="asdasd@gmail.com", first_name='qweqwe', last_name='qwqweqwe', password='qweqweqw'))
    db.session.add(User(email="kamilm215@gmail.com", first_name='Kamil', last_name='Misiak', password='qwe123', admin=1))
    db.session.add(User(email="seba___stian@wp.pl", first_name='Sebastian', last_name='Kania', password='qwerty123', admin=1))
    db.session.commit()

@cli.command()
def cov():
    tests = unittest.TestLoader().discover('project/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    sys.exit(result)


if __name__ == '__main__':
    cli()