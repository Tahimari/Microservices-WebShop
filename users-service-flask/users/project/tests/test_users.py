import json
import unittest

from project.tests.base import BaseTestCase
from project import db
from project.api.models import User

def add_user(email, first_name, last_name, password):
    user = User(email=email, first_name=first_name, last_name=last_name, password=password)
    db.session.add(user)
    db.session.commit()
    return user

class TestUserService(BaseTestCase):

    def test_users(self):
        response = self.client.get('/users/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])


    def test_encode_auth_token(self):
        user = User(
            first_name='Michael',
            last_name='Herman',
            email='test@test.com',
            password='test'
        )
        db.session.add(user)
        db.session.commit()
        auth_token = user.encode_auth_token(user.id, user.admin)
        self.assertTrue(isinstance(auth_token, bytes))
        

if __name__ == '__main__':
    unittest.main()
