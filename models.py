from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'hero'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    super_name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    powers = db.relationship("Hero_powers", backref="hero")

    @validates('name', 'super_name')
    def validate_name(self, key, value):
        if not value:
            raise ValueError(f"'{key}' cannot be empty.")
        return value

class Hero_powers(db.Model):
    __tablename__ = 'hero_powers'
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(100))
    hero_id = db.Column(db.Integer, db.ForeignKey("hero.id"))
    power_id = db.Column(db.Integer, db.ForeignKey("powers.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @validates('strength')
    def validate_strength(self, key, value):
        if not value:
            raise ValueError("'strength' cannot be empty.")
        return value

class Powers(db.Model):
    __tablename__ = 'powers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    heroes = db.relationship("Hero_powers", backref="power")

    @validates('name', 'description')
    def validate_name_description(self, key, value):
        if not value:
            raise ValueError(f"'{key}' cannot be empty.")
        return value
