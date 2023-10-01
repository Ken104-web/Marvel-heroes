from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# add any models you may need. 
class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    created_at = db.Column(db.DateTime,server_default=db.func.now())
    updated_at = db.Column(db.DateTime,onupdate=db.func.now())

    # - A Hero has many Power`s through HeroPower
    powers = db.relationship('Power', secondary = 'hero_powers', back_populates="heroes")


class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime,server_default=db.func.now())
    updated_at = db.Column(db.DateTime,onupdate=db.func.now())

    #  A Power has many Hero`s through HeroPower

    heroes = db.relationship('Hero', secondary = "hero_powers", back_populates="powers")
class HeroPower(db.Model):
    __tablename__ = 'hero_powers'
    id = db.Column(db.Integer, primary_key=True)
    strength =db.Column(db.String)

    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    powers_id = db.Column(db.Integer, db.ForeignKey('powers.id'))

    created_at = db.Column(db.DateTime,server_default=db.func.now())
    updated_at = db.Column(db.DateTime,onupdate=db.func.now())


    

