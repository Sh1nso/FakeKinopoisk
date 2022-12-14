from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_all(self):
        return self.session.query(User).all()

    def get_user_by_email(self, email):
        return self.session.query(User).filter(User.email == email).first()

    def create(self, user_d):
        user = User(**user_d)
        self.session.add(user)
        self.session.commit()
        return user

    def update_pass(self, user_d):
        user = self.get_user_by_email(user_d["email"])
        user.password = user_d.get("password_2")

        self.session.add(user)
        self.session.commit()

    def update(self, user):
        self.session.add(user)
        self.session.commit()
        return user

    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()
