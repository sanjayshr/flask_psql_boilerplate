from flask import Blueprint, jsonify, request
from app.models.user import User
from app.database import db

user = Blueprint('user', __name__)

@user.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@user.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    user = User()
    user.username = data.get('username')
    user.email = data.get('email')
    user.set_password(data.get('password'))
    user.from_dict(data)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201