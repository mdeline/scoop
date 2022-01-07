# Application initialization, app.py or app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    # Create Flask application.
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    # Initialize database
    db.init_app(app)

    with app.app_context():
        # Import parts of our application
        from .home import home
        from .login import login
        from .register import register
        from .discover import discover
        from . import forms

        # Register Blueprints
        app.register_blueprint(home.home_bp)
        app.register_blueprint(home.result_bp)
        app.register_blueprint(login.login_pb)
        app.register_blueprint(register.register_pb)
        app.register_blueprint(register.success_pb)
        app.register_blueprint(discover.discover_pb)

        return app