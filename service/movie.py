from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_query(self):
        return self.dao.get_query()

    def get_all(self):
        return self.dao.get_all()

    def get_ordered(self):
        return self.dao.get_all_ordered()

    def get_paginate(self, page):
        return self.dao.paginate_all(int(page)).items

    def create(self, movie_d):
        return self.dao.create(movie_d)

    def update(self, movie_d):
        self.dao.update(movie_d)
        return self.dao

    def delete(self, rid):
        self.dao.delete(rid)
