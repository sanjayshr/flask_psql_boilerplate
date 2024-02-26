from flask import Blueprint, jsonify
from app.services.hello_service import hello as hello_service

hello = Blueprint('hello', __name__)

@hello.route('/api/test', methods=['GET'])
def test():
    return jsonify(hello_service())