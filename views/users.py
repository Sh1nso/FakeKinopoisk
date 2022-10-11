from flask import request
from flask_restx import Resource, Namespace

from implemented import user_service

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    def post(self):
        req_data = request.json
        user = user_service.create(req_data)
        return 'Спасибо за регистрацию', 201


@user_ns.route('/password')
class UserPasswordView(Resource):
    def put(self):
        req_data = request.json
        user = user_service.update_password(req_data)
        return 'Пароль обновлен', 201
