# imports
import types
from flask import Blueprint

from app.decorators import class_route

sales = Blueprint("sales", __name__, url_prefix="/sales", template_folder="templates")

sales.class_route = types.MethodType(class_route, sales)

from .views import InvoiceView
