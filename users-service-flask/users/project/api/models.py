from sqlalchemy.sql import func
import datetime
from project import db

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, email, first_name, last_name, password, admin=False):
        self.email = email,
        self.first_name = first_name,
        self.last_name = last_name,
        self.password = password
        self.registered_on = datetime.datetime.now()
        self.admin = admin

    def to_json(self):
        return {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password': self.password
        }