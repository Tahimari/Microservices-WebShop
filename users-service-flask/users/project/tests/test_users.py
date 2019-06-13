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
    """Tests for the Users Service."""

    def test_users(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get('/users/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])

    def test_single_user(self):
        """Ensure get single user behaves correctly."""
        user = add_user('michael@mherman.org', 'michael', 'Herman', 'qwerty123456')
        with self.client:
            response = self.client.get(f'/users/{user.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('michael', data['data']['first_name'])
            self.assertIn('michael@mherman.org', data['data']['email'])
            self.assertIn('success', data['status'])

    def test_single_user_no_id(self):
        """Ensure error is thrown if an id is not provided."""
        with self.client:
            response = self.client.get('/users/blah')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('User does not exist', data['message'])
            self.assertIn('fail', data['status'])

    def test_single_user_incorrect_id(self):
        """Ensure error is thrown if the id does not exist."""
        with self.client:
            response = self.client.get('/users/999')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('User does not exist', data['message'])
            self.assertIn('fail', data['status'])

    def test_all_users(self):
        """Ensure get all users behaves correctly."""
        add_user('michael@mherman.org', 'michael', 'Herman', 'qwerty123456')
        add_user('fletcher@notreal.com', 'fletcher', 'Herman', 'qwerty123456')
        with self.client:
            response = self.client.get('/users')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['users']), 2)
            self.assertIn('michael', data['users'][0]['first_name'])
            self.assertIn(
                'michael@mherman.org', data['users'][0]['email'])
            self.assertIn('fletcher', data['users'][1]['first_name'])
            self.assertIn(
                'fletcher@notreal.com', data['users'][1]['email'])
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
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))


    def test_decode_auth_token(self):
        user = User(
            first_name='Michael',
            last_name='Herman',
            email='test@test.com',
            password='test'
        )
        db.session.add(user)
        db.session.commit()
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertTrue(User.decode_auth_token(
            auth_token.decode("utf-8")) == 1)
        

if __name__ == '__main__':
    unittest.main()
