# imports
from flask import render_template as render
from flask.views import View

class WelcomeView(View):
    def dispatch_request(self):
        # DB
        products = [
            {"id": 1, "name": "Televisor", "description": None, "category_id": 1, "category_name": "Electrodomesticos"},
            {"id": 2, "name": "Nevera", "description": None, "category_id": 1, "category_name": "Electrodomesticos"},
            {"id": 3, "name": "Lavadora", "description": None, "category_id": 1, "category_name": "Electrodomesticos"},
            {"id": 4, "name": "Escritorio de Madera", "description": None, "category_id": 2, "category_name": "Muebles"}
        ]
        services = [
            {"id": 1, "name": "Ventas Online"},
            {"id": 2, "name": "Compras Online"}
        ]
        context = {
             "services": services,
             "products": products
        }

        return render("pages/welcome.html", **context)