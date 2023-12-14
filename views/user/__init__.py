from flask import Blueprint
from flask_app.views.user.user_view import UserView

user_view = UserView()
user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/register", methods=["GET"])
def register(): return user_view.register()

@user_routes.route("/create", methods=["POST"])
def create(): return user_view.create()

@user_routes.route("/login-form", methods=["GET"])
def login_form(): return user_view.login_form()

@user_routes.route("/login", methods=["POST"])
def login(): return user_view.login()

@user_routes.route("/logout", methods=["GET"])
def logout(): return user_view.logout()