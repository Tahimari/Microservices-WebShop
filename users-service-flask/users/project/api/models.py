from sqlalchemy.sql import func
import datetime
import jwt
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

    def encode_auth_token(self, user_id):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
                'iat': datetime.datetime.utcnow(),
                'customer_id': user_id
            }
            return jwt.encode(
                payload,
                "secret",
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, "secret")
            return payload['customer_id']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'