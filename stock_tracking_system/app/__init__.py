
"""
Initialize the Flask application and configure extensions.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_mail import Mail

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    mail.init_app(app)

    from .routes import product_routes, supplier_routes, user_routes, sale_routes
    app.register_blueprint(product_routes.bp)
    app.register_blueprint(supplier_routes.bp)
    app.register_blueprint(user_routes.bp)
    app.register_blueprint(sale_routes.bp)

    return app
