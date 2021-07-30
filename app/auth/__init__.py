# imports
import types
from flask import Blueprint

from app.decorators import class_route

auth = Blueprint("auth", __name__, url_prefix="/auth", template_folder="templates")

auth.class_route = types.MethodType(class_route, auth)

from .views import LoginView
