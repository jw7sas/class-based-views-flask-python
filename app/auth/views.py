# imports
from . import *
from flask import render_template as render, request, flash, redirect, url_for
from flask.views import View

""" Clase para generar la vista de Login. """
@auth.class_route("/login", "login_view")
class LoginView(View):
    methods=['GET', 'POST']

    def dispatch_request(self):
        data = {
            "username": "as_geek",
            "password": "123Admin"
        }
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            if (not username) or (not password):
                flash("Campos vacíos completelos por favor!")
            elif data["username"] == username and data["password"] == password:
                return redirect(url_for("welcome_view"))
            else:
                flash("Usuario y/o contraseña incorrectos!!")
            
        return render("pages/login.html")