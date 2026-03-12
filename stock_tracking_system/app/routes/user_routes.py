
"""
Routes for user management.
"""

from flask import Blueprint, jsonify, request
from ..models import User
from .. import db

bp = Blueprint('user', __name__, url_prefix='/users')

@bp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.username for user in users])

@bp.route('/', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(username=data['username'], password=data['password'], role=data['role'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added'}), 201
