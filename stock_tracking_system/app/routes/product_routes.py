
"""
Routes for product management.
"""

from flask import Blueprint, jsonify, request
from ..models import Product
from .. import db

bp = Blueprint('product', __name__, url_prefix='/products')

@bp.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.name for product in products])

@bp.route('/', methods=['POST'])
def add_product():
    data = request.get_json()
    new_product = Product(name=data['name'], price=data['price'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product added'}), 201
