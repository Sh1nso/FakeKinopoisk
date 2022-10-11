from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        # доделать пагинацию
        status = request.args.get("status")
        page = request.args.get("page")
        data = movie_service.get_query()
        if status is not None:
            data = movie_service.get_ordered()
        if page is not None:
            data = movie_service.get_paginate(page)
        data = MovieSchema(many=True).dump(data)
        return data, 200


@movie_ns.route('/<int:bid>')
class MovieView(Resource):
    def get(self, bid):
        b = movie_service.get_one(bid)
        sm_d = MovieSchema().dump(b)
        return sm_d, 200
