import hashlib

from constans import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.user import UserDAO


class UserService:

    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def get_user_by_username(self, email):
        return self.dao.get_user_by_email(email)

    def check_uniq_user(self, user_d):
        user = self.get_user_by_username(user_d['email'])
        if user is None:
            return False
        return True

    def create(self, user_d):
        user_pass = user_d.get('password')
        user_hashed_pass = self.get_hash(user_pass)
        user_d['password'] = user_hashed_pass
        return self.dao.create(user_d)

    def update_password(self, user_d):
        user_email = user_d.get('user_email')
        user_pass_old = user_d.get('password_1')
        user_pass_new = user_d.get('password_2')
        pass

    def patch_update(self, user_d):
        email = user_d.get('email', None)
        name = user_d.get('name', None)
        surname = user_d.get('surname', None)
        genre_id = user_d.get('genre_id', None)
        if email is not None:
            user = self.get_user_by_username(email)
            if name is not None:
                user.name = name
            if surname is not None:
                user.surname = surname
            if genre_id is not None:
                user.genre_id = genre_id
            return self.dao.update(user)
        return False

    def delete(self, uid):
        return self.dao.delete(uid)

    def get_hash(self, password):
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ).decode("utf-8", "ignore")
