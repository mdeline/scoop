# Application initialization, app.py or app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    # Create Flask application.
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    # Initialize Plugins
    db.init_app(app)

    with app.app_context():
        # Import parts of our application
        from .home import home
        from .venue import venue
        from .auth import auth
        from .discover import discover
        from . import forms

        # Register Blueprints
        app.register_blueprint(home.home_bp)
        app.register_blueprint(venue.venue_bp, url_prefix='/venue')
        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(discover.discover_pb)

        return app