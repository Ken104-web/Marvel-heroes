#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request, render_template
from flask_migrate import Migrate
from flask_restful import Api, Resource
from dotenv import load_dotenv
load_dotenv()

from models import db, Hero, Power, HeroPower

app = Flask(
    __name__,
    static_url_path='',
    static_folder='../client/build',
    template_folder='../client/build'
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

@app.errorhandler(404)
def not_found(e):
    return render_template("index.html")
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

class EachHero(Resource):
     def get(self, id):
        each_hero = Hero.query.filter_by(id=id).first()
        if each_hero:
            hero_data = each_hero.to_dict()
            resp = make_response(
                hero_data,
                200,
            )
            return resp
        else:
            raise ValueError("Hero not found")
api.add_resource(EachHero, '/heroes/<int:id>')

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
class PostHeroPower(Resource):
    def post(self):
        data = request.get_json()        
        hero_power = HeroPower(
            strength=data['id'],
            power_id=['power_id'],
            hero_id=data['hero_id'],
        )
        db.session.add(hero_power)
        db.session.commit()
        return make_response(hero_power.to_dict(), 201)
    
api.add_resource(PostHeroPower, '/heropower')

if __name__ == '__main__':
    app.run(port=5555)
