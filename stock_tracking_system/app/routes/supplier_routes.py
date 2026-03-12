
"""
Routes for supplier management.
"""

from flask import Blueprint, jsonify, request
from ..models import Supplier
from .. import db

bp = Blueprint('supplier', __name__, url_prefix='/suppliers')

@bp.route('/', methods=['GET'])
def get_suppliers():
    suppliers = Supplier.query.all()
    return jsonify([supplier.name for supplier in suppliers])

@bp.route('/', methods=['POST'])
def add_supplier():
    data = request.get_json()
    new_supplier = Supplier(name=data['name'])
    db.session.add(new_supplier)
    db.session.commit()
    return jsonify({'message': 'Supplier added'}), 201
