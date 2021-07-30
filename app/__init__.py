# imports
from flask import Flask
from app.routes import Routes
from .auth import auth
from .sales import sales
from .config import Config


def create_app():
    """ Método de configuración de APP. """
    app = Flask(__name__)
    # configuración básica
    app.config.from_object(Config)

    # Manejo de rutas
    routes = Routes(app)
    app = routes.getRoutes()

    # Vistas con  blueprints
    app.register_blueprint(auth)
    app.register_blueprint(sales)

    return app