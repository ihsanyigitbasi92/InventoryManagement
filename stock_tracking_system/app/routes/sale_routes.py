
"""
Routes for sales management.
"""

from flask import Blueprint, jsonify, request
from ..models import Sale
from .. import db

bp = Blueprint('sale', __name__, url_prefix='/sales')

@bp.route('/', methods=['GET'])
def get_sales():
    sales = Sale.query.all()
    return jsonify([sale.id for sale in sales])

@bp.route('/', methods=['POST'])
def add_sale():
    data = request.get_json()
    new_sale = Sale(product_id=data['product_id'], quantity=data['quantity'], total_price=data['total_price'])
    db.session.add(new_sale)
    db.session.commit()
    return jsonify({'message': 'Sale added'}), 201
