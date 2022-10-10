from marshmallow import Schema, fields

from setup_db import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=True)
    surname = db.Column(db.String, nullable=True)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"), nullable=True)
    favorite_genre = db.relationship("Genre")


class UserSchema(Schema):
    username = fields.Str()
    password = fields.Str()
    role = fields.Str()
