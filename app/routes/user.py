from flask import Blueprint, jsonify, request
from app.services.user_service import get_all_users, create_new_user

user = Blueprint('user', __name__)

@user.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(get_all_users())

@user.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    new_user =  create_new_user(data)
    return jsonify(new_user), 201
    