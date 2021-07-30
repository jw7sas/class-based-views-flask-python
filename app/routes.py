# imports
from app.views import WelcomeView

""" Clase para retornar rutas del sistema. """
class Routes():
    def __init__(self, app):
        super().__init__()
        self.app = app

    def getRoutes(self):
        self.getAppRoutes()

        return self.app

    def getAppRoutes(self):
        """ Método para generar rutas del proyecto app. """
        self.app.add_url_rule('/welcome', view_func=WelcomeView.as_view('welcome_view'))