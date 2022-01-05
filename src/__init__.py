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
        from .login import login
        from .register import register
        from . import forms

        # Register Blueprints
        app.register_blueprint(home.home_bp)
        app.register_blueprint(login.login_pb)
        app.register_blueprint(register.register_pb)
        app.register_blueprint(register.success_pb)

        return app