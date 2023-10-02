from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
db = SQLAlchemy()

# add any models you may need. 
class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'

    serialize_rules = ('-powers',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    created_at = db.Column(db.DateTime,server_default=db.func.now())
    updated_at = db.Column(db.DateTime,onupdate=db.func.now())

    # - A Hero has many Power`s through HeroPower
    powers = db.relationship('Power', secondary = 'hero_powers', back_populates="heroes")

    
class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'
    serialize_rules = ('-hero.powers',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime,server_default=db.func.now())
    updated_at = db.Column(db.DateTime,onupdate=db.func.now())

    #  A Power has many Hero`s through HeroPower

    heroes = db.relationship('Hero', secondary = "hero_powers", back_populates="powers")
    
    @validates('description')
    def validate_description(self, key, description):
        if len(description) < 20:
            raise ValueError("Description not enough")
        return description
class HeroPower(db.Model):
    __tablename__ = 'hero_powers'
    id = db.Column(db.Integer, primary_key=True)
    strength =db.Column(db.String)

    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    powers_id = db.Column(db.Integer, db.ForeignKey('powers.id'))

    created_at = db.Column(db.DateTime,server_default=db.func.now())
    updated_at = db.Column(db.DateTime,onupdate=db.func.now())

    @validates('strength')
    def validate_strength(self, key, strength):
        valid_strengths = ['Strong', 'Weak', 'Average']
        if strength not in valid_strengths:
            raise ValueError("Must be one of: 'Strong', 'Weak', 'Average'")
        return strength
    

