#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Home(Resource):
    def get(self):
        resp_dict = {
            "Home": "Home to Marvel heroes"
        }
        resp = make_response(
            jsonify(resp_dict),
            200,
        )
        return resp
api.add_resource(Home, '/')

class HeroNames(Resource):
    def get(self):
        heroes = [hero.to_dict() for hero in Hero.query.all()]
        resp = make_response(
            jsonify(heroes),
            200,
        )
        return resp
api.add_resource(HeroNames, '/heroes')

class GetPowers(Resource):
    def get(self):
        powers = [power.to_dict() for power in Power.query.all()]

        resp = make_response(
            jsonify(powers),
            200,
        )
        return resp

api.add_resource(GetPowers, '/powers')

class GetEachPower(Resource):
    def get(self, id):
        each_power = Power.query.filter_by(id=id).first()
        if each_power:
            power_data = each_power.to_dict()
            resp = make_response(
                power_data,
                200,
            )
            return resp
        else:
            raise ValueError("Power not found")
    def patch(self, id):
        updatePower = Power.query.filter_by(id=id).first()
        for attr in request.form:
            setattr(updatePower, attr, request.form[attr])

        db.session.add(updatePower)
        db.session.commit()
        resp_dict = updatePower.to_dict()
        resp =make_response(
            jsonify(resp_dict),
            200
        )
        return resp
api.add_resource(GetEachPower, '/powers/<int:id>')



if __name__ == '__main__':
    app.run(port=5555)
