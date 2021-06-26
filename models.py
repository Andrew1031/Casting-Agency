import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json
from config import SQLALCHEMY_DATABASE_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
# database_filename = "database.db"
# project_dir = os.path.dirname(os.path.abspath(__file__))
# database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))

db = SQLAlchemy()

def setup_db(app, database_path=SQLALCHEMY_DATABASE_URI):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

def db_drop_and_create_all():
    db.drop_all()
    db.create_all()

def db_drop_and_create_all_defaults():
    db.drop_all()
    db.create_all()
    actor = Actor(name="Scarlett Johansson", age=36, gender="Female")
    actor.insert()
    movie = Movie(title="Black Widow", release="2021")
    movie.insert()

class Actor(db.Model):
    __tablename__ = 'actors'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String)
    age = db.Column(Integer)
    gender = db.Column(db.String)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(Integer, primary_key=True)
    title = db.Column(String)
    release = db.Column(String)

    def __init__(self, title, release):
        self.title = title
        self.release = release

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release': self.release
        }