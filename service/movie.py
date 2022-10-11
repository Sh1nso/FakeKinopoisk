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
        return self.dao.paginate_all(int(page))
    # доделать пагинацю
    # def get_all(self, filters):
    #     movies = self.dao.get_all()
    #     if filters.get("status") is not None and filters.get("status") == "new":
    #         movies = self.dao.get_all_ordered()
    #     if filters.get("page") is not None:
    #         movies = movies.paginate(page=filters.get('page'),per_page=12)
    #     return movies

    def create(self, movie_d):
        return self.dao.create(movie_d)

    def update(self, movie_d):
        self.dao.update(movie_d)
        return self.dao

    def delete(self, rid):
        self.dao.delete(rid)
