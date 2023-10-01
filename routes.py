from flask import jsonify,request
from app import app,Resource,api
from models import db,Hero,Hero_powers,Powers

from flask import Flask, jsonify, make_response

@app.route('/heroes',methods=['GET'])
def get_heroes():
    heroes = []
    for heros in Hero.query.all():
        user_object = {
            'id': heros.id,
            'name':heros.name,
            'super_name':heros.super_name
        }

    heroes.append(user_object)

    return jsonify(heroes)


@app.route('/heroes/<int:id>',methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)

    if hero:
        hero_data = {
            'id': hero.id,
            'name': hero.name,
            'super_name': hero.super_name
        }
        return jsonify(hero=hero_data), 200
    else:
        return jsonify(message='Hero not found'), 404



@app.route('/powers',methods=['GET'])
def get_powers():
    power=[]
    for powers in Powers.query.all():
        powers_object = {
        'id':powers.id,
        'name':powers.name,
        'description':powers.description
    }
    power.append(powers_object)
    return jsonify(power),200

@app.route('/powers/<int:id>',methods=['GET'])
def get_power_id(id):
    power = Powers.query.get(id)

    if power:
        power_data = {
            'id': power.id,
            'name': power.name,
            'description': power.description
        }
        return jsonify(power=power_data), 200
    else:
        return jsonify(message='Power not found'), 404


@app.route('/powers/<int:id>',methods=['PATCH'])
def update_power(id):
    data = request.get_json()
    power = Powers.query.get(id)

    if power:
        original_description = power.description
        new_description = data.get('description', original_description)
        power.description = new_description
        db.session.commit()

        # Construct the response JSON with the requested format
        response_data = {
            'id': power.id,
            'name': power.name,
            'description': new_description
        }

        return jsonify(response_data), 200
    else:
        error_response = {
            'error': 'Power not found'
        }
        return jsonify(error_response), 404
    
@app.route('/hero_powers', methods=['POST'])
def create_hero_powers():
    data = request.get_json()
    new_hero_powers = Hero_powers(
        strength=data['strength'],
        hero_id = data['hero_id'],
        power_id = data['power_id']
    )

    db.session.add(new_hero_powers)
    db.session.commit()
    return jsonify({
        "id": new_hero_powers.id,
        "strength": new_hero_powers.strength,
        "hero_id": new_hero_powers.hero_id,
        "power_id": new_hero_powers.power_id
        }), 201













