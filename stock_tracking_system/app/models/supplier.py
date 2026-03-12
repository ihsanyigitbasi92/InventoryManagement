
"""
Supplier model for managing supplier details.
"""

from . import db

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    contact_info = db.Column(db.String(200))

    def __repr__(self):
        return f'<Supplier {self.name}>'
