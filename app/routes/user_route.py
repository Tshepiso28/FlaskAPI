from flask import Blueprint, request, jsonify
from app.controller.user_controller import UserController

user_blueprint = Blueprint('user_routes', __name__)

@user_blueprint.route('/', methods=['GET'])
def get_users():
    users = UserController.get_users()
    return jsonify(users)

@user_blueprint.route('/add', methods=['POST'])
def add_user():
    data = request.get_json()
    UserController.add_user(data['name'], data['email'], data['password_hash'])
    return jsonify({'message': 'User added successfully'}), 201

@user_blueprint.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    UserController.delete_user(user_id)
    return jsonify({'message': 'User deleted successfully'})