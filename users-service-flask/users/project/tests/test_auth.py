import unittest
import json
import time


from project import db
from project.api.models import User, BlacklistToken
from project.tests.base import BaseTestCase


def register_user(self, email, first_name, last_name, password):
    return self.client.post(
        '/users',
        data=json.dumps(dict(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )),
        content_type='application/json',
    )


class TestAuthBlueprint(BaseTestCase):
    def test_registration(self):
        with self.client:
            response = register_user(self, 'joe@gmail.com', 'Michael', 'Herman', '123456')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'joe@gmail.com was added!')
            self.assertTrue(data['token'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)


    def test_registration_invalid_json(self):
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({}),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])


    def test_registration_invalid_json_keys(self):
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({'email': 'michael@mherman.org'}),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])


    def test_registered_with_already_registered_user(self):
        user = User(
            email='joe@gmail.com',
            first_name='Michael',
            last_name='Herman',
            password='test'
        )
        db.session.add(user)
        db.session.commit()
        with self.client:
            response = register_user(self, 'joe@gmail.com', 'Michael', 'Herman', '123456')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(
                data['message'] == 'Sorry. That email already exists.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 202)


    def test_registered_user_login(self):
        with self.client:
            resp_register = register_user(self, 'joe@gmail.com', 'Michael', 'Herman', '123456')
            data_register = json.loads(resp_register.data.decode())
            self.assertTrue(data_register['status'] == 'success')
            self.assertTrue(
                data_register['message'] == 'joe@gmail.com was added!'
            )
            self.assertTrue(data_register['token'])
            self.assertTrue(resp_register.content_type == 'application/json')
            self.assertEqual(resp_register.status_code, 201)
            response = self.client.post(
                '/users/login',
                data=json.dumps(dict(
                    email='joe@gmail.com',
                    first_name='Michael',
                    last_name='Herman',
                    password='123456'
                )),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully logged in.')
            self.assertTrue(data['token'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)



    def test_non_registered_user_login(self):
        with self.client:
            response = self.client.post(
                '/users/login',
                data=json.dumps(dict(
                    email='joe@gmail.com',
                    first_name='Michael',
                    last_name='Herman',
                    password='123456'
                )),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(data['message'] == 'Try again')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 404)


    def test_valid_logout(self):
        with self.client:
            resp_register = register_user(self, 'joe@gmail.com', 'Michael', 'Herman', '123456')
            data_register = json.loads(resp_register.data.decode())
            self.assertTrue(data_register['status'] == 'success')
            self.assertTrue(
                data_register['message'] == 'joe@gmail.com was added!')
            self.assertTrue(data_register['token'])
            self.assertTrue(resp_register.content_type == 'application/json')
            self.assertEqual(resp_register.status_code, 201)
            resp_login = self.client.post(
                '/users/login',
                data=json.dumps(dict(
                    email='joe@gmail.com',
                    first_name='Michael',
                    last_name='Herman',
                    password='123456'
                )),
                content_type='application/json'
            )
            data_login = json.loads(resp_login.data.decode())
            self.assertTrue(data_login['status'] == 'success')
            self.assertTrue(data_login['message'] == 'Successfully logged in.')
            self.assertTrue(data_login['token'])
            self.assertTrue(resp_login.content_type == 'application/json')
            self.assertEqual(resp_login.status_code, 200)
            response = self.client.post(
                '/users/logout',
                headers=dict(
                    Authorization='Bearer ' + json.loads(
                        resp_login.data.decode()
                    )['token']
                )
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully logged out.')
            self.assertEqual(response.status_code, 200)


    def test_valid_blacklisted_token_logout(self):
        with self.client:
            resp_register = register_user(self, 'joe@gmail.com', 'Michael', 'Herman', '123456')
            data_register = json.loads(resp_register.data.decode())
            self.assertTrue(data_register['status'] == 'success')
            self.assertTrue(
                data_register['message'] == 'joe@gmail.com was added!')
            self.assertTrue(data_register['token'])
            self.assertTrue(resp_register.content_type == 'application/json')
            self.assertEqual(resp_register.status_code, 201)
            resp_login = self.client.post(
                '/users/login',
                data=json.dumps(dict(
                    email='joe@gmail.com',
                    first_name='Michael',
                    last_name='Herman',
                    password='123456'
                )),
                content_type='application/json'
            )
            data_login = json.loads(resp_login.data.decode())
            self.assertTrue(data_login['status'] == 'success')
            self.assertTrue(data_login['message'] == 'Successfully logged in.')
            self.assertTrue(data_login['token'])
            self.assertTrue(resp_login.content_type == 'application/json')
            self.assertEqual(resp_login.status_code, 200)
            blacklist_token = BlacklistToken(
                token=json.loads(resp_login.data.decode())['token'])
            db.session.add(blacklist_token)
            db.session.commit()
            response = self.client.post(
                '/users/logout',
                headers=dict(
                    Authorization='Bearer ' + json.loads(
                        resp_login.data.decode()
                    )['token']
                )
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(data['message'] == 'Token blacklisted. Please log in again.')
            self.assertEqual(response.status_code, 401)


if __name__ == '__main__':
    unittest.main()