from flask import Blueprint
from flask_app.views.home.home import Home

home = Home()
home_routes = Blueprint('home', __name__)

@home_routes.route("/", methods=["GET"])
def index(): return home.index()
