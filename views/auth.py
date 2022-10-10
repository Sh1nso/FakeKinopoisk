from flask import request
from flask_restx import Resource, Namespace

from implemented import user_service
from service.jwt_service import jwt_object

auth_ns = Namespace('auth')


@auth_ns.route('/login/')
class AuthView(Resource):
    def post(self):
        tokens = jwt_object.give_user_jwt_token()
        return tokens, 201

    def put(self):
        tokens = jwt_object.check_refresh_token()
        return tokens, 201


@auth_ns.route('/register/')
class RegisterView(Resource):
    def post(self):
        req_user = request.json
        if req_user is None:
            return 'Введите необходимые данные', 404
        email = req_user.get('email', None)
        password = req_user.get('password', None)
        if None in [email, password]:
            return 'Введите необходимые данные', 404
        user = user_service.create(req_user)
        return 201
