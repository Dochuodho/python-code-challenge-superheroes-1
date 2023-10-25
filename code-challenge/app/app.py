#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from flask_restful import Resource, Api

from models import db, Hero, HeroPower,Power

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = True

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return 'Superheroes API'


class Heroes(Resource):
    def get(self):
        heroes = []
        for hero in Hero.query.all():
            hero_dict = {
                "id": hero.id,
                "name": hero.name,
                "super_name": hero.super_name
            }
            heroes.append(hero_dict)

        return make_response(jsonify(heroes), 200)


if __name__ == '__main__':
    app.run(port=5555)
