# routes.py

from flask import jsonify, request
from models import User, db, bcrypt
from flask_restful import Resource

class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if user:
            return jsonify(user.serialize()), 200
        else:
            return jsonify({'error': 'User not found'}), 404

    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify(user.serialize()), 201
    
class Signup(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password=hashed_password)
        try:
            db.session.add(new_user)
            db.session.commit()
            db.sections['user_id'] = new_user.id
            return jsonify(new_user.serialize()), 201
        except IntegrityError:
            db.session.rollback()
            return jsonify({'error': 'Username already exists'}), 422


# Define other routes similarly for RecipeResource, etc.
