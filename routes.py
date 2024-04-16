# routes.py

from flask import jsonify, request
from models import User, db
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

