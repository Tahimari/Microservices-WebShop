from flask import Blueprint, request, render_template
from flask_restful import Resource, Api
from sqlalchemy import exc
from flask_mail import Message

from project import db, mail
from project.api.models import User, BlacklistToken


users_blueprint = Blueprint('users', __name__, template_folder='./templates')
api = Api(users_blueprint)


class UsersPing(Resource):
    def get(self):
        return  {
            'status': 'success',
            'message': 'pong!'
        }


class UserRegister(Resource):
    def post(self):
        post_data = request.get_json()
        response_object = {
            'status': 'fail',
            'message': 'Invalid payload.'
        }
        if not post_data:
            return response_object, 400
        email = post_data.get('email')
        first_name = post_data.get('first_name')
        last_name = post_data.get('last_name')
        password = post_data.get('password')
        try:
            user = User.query.filter_by(email=email).first()
            if not user:
                user = User(email=email, first_name=first_name, last_name=last_name, password=password)
                db.session.add(user)
                db.session.commit()
                auth_token = user.encode_auth_token(user.id, user.admin)
                response_object['status'] = 'success'
                response_object['message'] = f'{email} was added!'
                response_object['token'] = auth_token.decode()
                return response_object, 201
            else:
                response_object['status'] = 'fail'
                response_object['message'] = 'Sorry. That email already exists.'
                return response_object, 202
        except exc.IntegrityError:
            db.session.rollback()
            return response_object, 400



# class Users(Resource):
#     def get(self, user_id):
#         response_object = {
#             'status': 'fail',
#             'message': 'User does not exist'
#         }
#         post_data = request.get_json()
#         try:
#             user = User.query.filter_by(id=int(user_id)).first()
#             if not user:
#                 return response_object, 404
#             else:
#                 response_object = {
#                     'status': 'success',
#                     'data': {
#                         'id': user.id,
#                         'email': user.email,
#                         'first_name': user.first_name,
#                         'last_name': user.last_name,
#                         'password': user.password
#                     }
#                 }
#                 return response_object, 200
#         except ValueError:
#             return response_object, 404

class UsersToken(Resource):
    def get(self):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                response_object = {
                    'status': 'fail',
                    'message': 'User does not exist'
                }
                try:
                    user = User.query.filter_by(id=int(resp['customer_id'])).first()
                    if not user:
                        return response_object, 404
                    else:
                        response_object = {
                            'status': 'success',
                            'data': {
                                'id': user.id,
                                'email': user.email,
                                'first_name': user.first_name,
                                'last_name': user.last_name,
                                'password': user.password,
                                'admin': user.admin,
                            }
                        }
                        return response_object, 200
                except ValueError:
                    return response_object, 404
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'Invalid jwt token'
                }
                return response_object, 404
        else:
            response_object = {
                'status': 'fail',
                'message': 'Jwt token not provided'
            }
            return response_object, 404




class LoginAPI(Resource):
    def post(self):
        post_data = request.get_json()
        try:
            user = User.query.filter_by(
                email=post_data.get('email')
              ).first()
            auth_token = user.encode_auth_token(user.id, user.admin)
            if auth_token and post_data.get('password')==user.password:
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully logged in.',
                    'token': auth_token.decode(),
                    'admin': user.admin
                }
                return responseObject, 200
            else:
                responseObject = {
                    'status': 'fail',
                    'message': 'Wrong credentials'
                }
                return responseObject, 401
        except Exception as e:
            print(e)
            responseObject = {
                'status': 'fail',
                'message': 'Try again'
            }
            return responseObject, 404


class LogoutAPI(Resource):
    def post(self):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                blacklist_token = BlacklistToken(token=auth_token)
                try:
                    db.session.add(blacklist_token)
                    db.session.commit()
                    responseObject = {
                        'status': 'success',
                        'message': 'Successfully logged out.'
                    }
                    return responseObject, 200
                except Exception as e:
                    responseObject = {
                        'status': 'fail',
                        'message': e
                    }
                    return responseObject, 200
            else:
                responseObject = {
                    'status': 'fail',
                    'message': resp
                }
                return responseObject, 401
        else:
            responseObject = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return responseObject, 403

class mailAPI(Resource):
    def post(self):
        post_data = request.get_json()
        response_object = {
            'status': 'fail',
            'message': 'Invalid payload.'
        }
        if not post_data:
            return response_object, 400
        email = post_data.get('email')
        name = post_data.get('name')
        message = post_data.get('message')
        response_object = {
            'email': email,
            'name': name,
            'message': message,
        }
        try:
            msg = Message(name,
                          sender=email,
                          recipients=['kamilm215@gmail.com'])
            msg.body = message
            mail.send(msg)
            response_object = {
                'status': 'success',
                'message': 'Mail sent.'
            }
            return  response_object, 200
        except Exception as e:
            return  str(e)


api.add_resource(UsersPing, '/users/ping')
api.add_resource(UserRegister, '/users')
#api.add_resource(Users, '/users/<user_id>')
api.add_resource(UsersToken, '/users/token')
api.add_resource(LoginAPI, '/users/login')
api.add_resource(LogoutAPI, '/users/logout')
api.add_resource(mailAPI, '/mail')
