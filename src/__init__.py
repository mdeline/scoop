# Application initialization
# app.py or app/__init__.py
from flask import Flask

def create_app():
    "Create Flask application."
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.config.from_pyfile('config.py') # Loads this if instance_relative_config is set to True

    with app.app_context():
        # Import parts of our application
        from .home import home

        # Register Blueprints
        app.register_blueprint(home.home_bp)

        return app