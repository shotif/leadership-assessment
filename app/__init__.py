from flask import Flask
from .routes import configure_routes


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'change-me'
    configure_routes(app)
    return app


__all__ = ["create_app"]
