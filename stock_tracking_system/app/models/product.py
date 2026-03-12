
"""
Product model for inventory management.
"""

from . import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200))
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)
    reorder_threshold = db.Column(db.Integer, default=10)

    def __repr__(self):
        return f'<Product {self.name}>'
