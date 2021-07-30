# imports
from flask import Flask

def create_app():
    """ Método de configuración de APP. """
    app = Flask(__name__)

    return app