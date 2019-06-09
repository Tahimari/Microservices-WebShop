from flask import Blueprint, request, render_template
from flask_restful import Resource, Api
from sqlalchemy import exc

from project import db
from project.api.models import User

users_blueprint = Blueprint('users', __name__, template_folder='./templates')
api = Api(users_blueprint)

class UsersPing(Resource):
    def get(self):
        return  {
            'status': 'success',
            'message': 'pong!'
        }

api.add_resource(UsersPing, '/users/ping')

class UsersList(Resource):
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
                db.session.add(User(email=email, first_name=first_name, last_name=last_name, password=password))
                db.session.commit()
                response_object['status'] = 'success'
                response_object['message'] = f'{email} was added!'
                return response_object, 201
            else:
                response_object['message'] = 'Sorry. That email already exists.'
                return response_object, 400
        except exc.IntegrityError:
            db.session.rollback()
            return response_object, 400

    def get(self):
        """Get all users"""
        response_object = {
            'status': 'success',
            'data': {
                'users': [user.to_json() for user in User.query.all()]
            }
        }
        return response_object, 200

api.add_resource(UsersList, '/users')

class Users(Resource):
    def get(self, user_id):
        """Get single user details"""
        response_object = {
            'status': 'fail',
            'message': 'User does not exist'
        }
        try:
            user = User.query.filter_by(id=int(user_id)).first()
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
                        'password': user.password
                    }
                }
                return response_object, 200
        except ValueError:
            return response_object, 404

api.add_resource(Users, '/users/<user_id>')

class LoginAPI(Resource):
    def post(self):
        post_data = request.get_json()
        try:
            user = User.query.filter_by(
                email=post_data.get('email')
              ).first()
            auth_token = user.encode_auth_token(user.id)
            if auth_token and post_data.get('password')==user.password:
                responseObject = {
                    'status': 'success',
                    'data': {
                        'message': 'Successfully logged in.',
                        'auth_token': auth_token.decode()
                    }
                }
                return responseObject, 200
            else:
                responseObject = {
                    'status': 'fail',
                    'data': {
                        'message': 'Wrong credentials'
                    }
                }
                return responseObject, 401
        except Exception as e:
            print(e)
            responseObject = {
                'status': 'fail',
                'data': {
                    'message': 'Try again'
                }
            }
            return responseObject, 500
api.add_resource(LoginAPI, '/users/login')

# class LogoutAPI(Resource):
#     def post(self):
#         auth_header = request.headers.get('Authorization')
#         if auth_header:
#             auth_token = auth_header.split(" ")[1]
#         else:
#             auth_token = ''
#         if auth_token:
#             resp = User.decode_auth_token(auth_token)
#             if not isinstance(resp, str):
#                 return False
#                 # blacklist_token = BlacklistToken(token=auth_token)
#                 # try:
#                 #     insert the token
#                 #     db.session.add(blacklist_token)
#                 #     db.session.commit()
#                 #     responseObject = {
#                 #         'status': 'success',
#                 #         'message': 'Successfully logged out.'
#                 #     }
#                 #     return responseObject, 200
#                 # except Exception as e:
#                 #     responseObject = {
#                 #         'status': 'fail',
#                 #         'message': e
#                 #     }
#                 #     return responseObject, 200
#             else:
#                 responseObject = {
#                     'status': 'fail',
#                     'message': resp
#                 }
#                 return responseObject, 401
#         else:
#             responseObject = {
#                 'status': 'fail',
#                 'message': 'Provide a valid auth token.'
#             }
#             return responseObject, 403
# api.add_resource(LogoutAPI, '/users/logout')

@users_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        db.session.add(User(email=email, first_name=first_name, last_name=last_name, password=password))
        db.session.commit()
    users = User.query.all()
    return render_template('index.html', users=users)