# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class Hero(db.Model):
#     __tablename__ = 'hero'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     super_name = db.Column(db.String(100), nullable=False)
#     powers = db.relationship("Hero_powers", backref="hero")

# class Hero_powers(db.Model):
#     __tablename__ = 'hero_powers'
#     id = db.Column(db.Integer, primary_key=True)
#     strength = db.Column(db.String(100))
#     hero_id = db.Column(db.Integer, db.ForeignKey("hero.id"))
#     power_id = db.Column(db.Integer, db.ForeignKey("powers.id"))

# class Powers(db.Model):
#     __tablename__ = 'powers'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.String(100), nullable=False)
#     heroes = db.relationship("Hero_powers", backref="power")

