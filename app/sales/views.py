# imports
import json

from . import *
from flask import jsonify, request
from flask.views import MethodView

""" Clase para generar las vistas API REST de Facturas. """
@sales.class_route("/invoice", "invoice_view", **{"pk": "invoice_id"})
class InvoiceView(MethodView):
    def get(self, invoice_id):
        sales = [
            {
                "id": 1, "details": [
                        {"id": 1, "product": {"id": 1, "name": "Televisor", "description": None, "category_id": 1, "category_name": "Electrodomesticos", "price": 1500000}, "units": 2},
                        {"id": 2, "product": {"id": 4, "name": "Escritorio de Madera", "description": None, "category_id": 2, "category_name": "Muebles", "price": 745000}, "units": 1}
                    ],
                "nFactura": 452635,
                "total": 3745000
            },
            {
                "id": 2, "details": [
                        {"id": 2, "product": {"id": 3, "name": "Lavadora", "description": None, "category_id": 1, "category_name": "Electrodomesticos", "price": 1213000}, "units": 1}
                    ],
                "nFactura": 452636,
                "total": 1213000
            }
        ]
        if invoice_id is None:
            # return a list of invoices
            return jsonify(sales)
        else:
            # expose a single invoice
            data = {}
            for sale in sales:
                if sale["id"] == invoice_id:
                    data = sale
            
            return jsonify(data)

    def post(self):
        # create a new invoice
        print("POST INFO ...")
        data = json.loads(request.data)
        response = {"code": "OK create", "method": "POST", "response": "Successfull!", "sale_id": None, "data": data}
        return jsonify(response)


    def delete(self, invoice_id):
        # delete a single invoice
        print("DELETE INFO ...")
        response = {"code": "OK delete", "method": "DELETE", "response": "Successfull!", "sale_id": invoice_id, "data": None}
        return jsonify(response)

    def put(self, invoice_id):
        # update a single invoice
        print("PUT INFO ...")
        data = json.loads(request.data)
        response = {"code": "OK update", "method": "PUT", "response": "Successfull!", "sale_id": invoice_id, "data": data}
        return jsonify(response)
